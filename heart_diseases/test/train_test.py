import os
import src
import unittest

INPUT_DATA_PATH = 'test/csv/test_train.csv'
OUTPUT_MODEL_PATH = 'test/models/model.pkl'
OUTPUT_METRIC_PATH = 'test/models/metric.json'
VAL_SIZE = 0.2
TARGET_COLUMN = 'condition'


def train() -> dict[str, float]:
    params = src.Params(
        input_data_path=INPUT_DATA_PATH,
        output_model_path=OUTPUT_MODEL_PATH,
        output_metric_path=OUTPUT_METRIC_PATH,
        val_size=VAL_SIZE,
        training_params=src.TrainingParams(),
        feature_params=src.FeatureParams(
            deleted_features=['fbs'],
            target_column='condition',
            normalize_features=['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
        )
    )
    return src.train(params)


class TrainTest(unittest.TestCase):
    def test_simple(self):
        metrics = train()
        self.assertGreaterEqual(metrics['accuracy'], 0)
        self.assertGreaterEqual(metrics['f1_score'], 0)
        self.assertTrue(os.path.exists(OUTPUT_MODEL_PATH))
        self.assertTrue(os.path.exists(OUTPUT_METRIC_PATH))
