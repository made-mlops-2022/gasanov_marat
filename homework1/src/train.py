import models
import sys
import data
import entities
import features
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def run_train_pipeline(config_path: str):
    params = entities.read_training_pipeline_params(config_path)
    train(params)


def train(params: entities.Params):
    logger.info(f"start train pipeline with params {params}")

    dataset = data.read_csv_data(params.input_data_path)
    logger.info(f"data.shape is {dataset.shape}")

    train_dataset, test_dataset = data.split_data(dataset, params.val_size)

    logger.info(f"train_df.shape is {train_dataset.shape}")
    logger.info(f"val_df.shape is {test_dataset.shape}")

    train_features, train_target = features.extract_target(train_dataset, params.feature_params.target_column)
    test_features, test_target = features.extract_target(test_dataset, params.feature_params.target_column)

    logger.info(f"train_features.shape is {train_features.shape}")
    logger.info(f"val_features.shape is {test_features.shape}")

    transformer = features.build_transformer(params.feature_params)
    train_features_transformed = transformer.fit_transform(train_features)

    model = models.train_model(train_features_transformed, train_target, params.training_params)

    inference_pipeline = models.create_inference_pipeline(model, transformer)

    models.serialize_model(model, output_path=params.output_model_path)
    predicted = models.predict_model(inference_pipeline, test_dataset)

    metrics = models.serialize_metric(predicted, test_target, params.output_metric_path)
    logger.info(f"metrics is {metrics}")

    models.serialize_model(inference_pipeline, params.output_model_path)
    return metrics


if __name__ == '__main__':
    run_train_pipeline(sys.argv[1])
