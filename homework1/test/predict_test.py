import os
import src
import unittest
from train_test import train

INPUT_DATA_PATH = 'test/csv/test_predict.csv'
INPUT_MODEL_PATH = 'test/models/model.pkl'
OUTPUT_DATA_PATH = 'test/models/predict.csv'


def predict() -> str:
    if not os.path.exists(INPUT_MODEL_PATH):
        train()
    return src.run_predict(INPUT_MODEL_PATH, INPUT_DATA_PATH, OUTPUT_DATA_PATH)


class PredictTest(unittest.TestCase):
    def test_predict(self):
        path = predict()
        self.assertTrue(os.path.exists(OUTPUT_DATA_PATH))
