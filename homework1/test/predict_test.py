import os
import src
import unittest

INPUT_DATA_PATH = 'test/csv/test_predict.csv'
INPUT_MODEL_PATH = 'test/models/model.pkl'
OUTPUT_DATA_PATH = 'test/models/predict.csv'


def predict() -> str:
    return src.run_predict(INPUT_MODEL_PATH, INPUT_DATA_PATH, OUTPUT_DATA_PATH)


class PredictTest(unittest.TestCase):
    def test_predict(self):
        path = predict()
        self.assertTrue(os.path.exists(OUTPUT_DATA_PATH))
