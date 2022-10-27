import models
import sys
import data
import entities
import features
import logging


def run_train_pipeline(config_path: str):
    params = entities.read_training_pipeline_params(config_path)
    feature = data.read_csv_data(params.input_data_path)
    train_dataset, test_dataset = data.split_data(feature, params.val_size)
    train_features, train_target = features.extract_target(train_dataset, params.target_column)
    test_features, test_target = features.extract_target(test_dataset, params.target_column)
    model = models.train_model(train_features, train_target)
    models.serialize_model(model, output_path=params.output_model_path)
    predicted = models.predict_model(model, test_features)
    models.serialize_metric(predicted, test_target, params.output_metric_path)
    models.serialize_model(model, params.output_model_path)


if __name__ == '__main__':
    run_train_pipeline(sys.argv[1])
