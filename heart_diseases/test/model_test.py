import unittest

import numpy as np

import src
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier


FEATURES = pd.DataFrame(np.zeros((3, 3)))
LABELS = pd.Series(np.arange(3))
FEATURES_TEST = pd.DataFrame(np.zeros((2, 3)))
TRUE_LABELS = pd.Series(np.zeros(2))
TRAINING_PARAMS = src.TrainingParams()


class TestTrain(unittest.TestCase):
    def test_simple(self):
        model = src.train_model(FEATURES, LABELS, TRAINING_PARAMS)
        self.assertIsInstance(model, GradientBoostingClassifier)


class TestPredict(unittest.TestCase):
    def test_simple(self):
        model = src.train_model(FEATURES, LABELS, TRAINING_PARAMS)
        predicted = src.predict_model(model, FEATURES_TEST)
        self.assertEqual(predicted.shape[0], 2)


class TestEvaluate(unittest.TestCase):
    def test_simple(self):
        model = src.train_model(FEATURES, LABELS, TRAINING_PARAMS)
        predicted = src.predict_model(model, FEATURES_TEST)
        metric = src.evaluate_model(predicted, TRUE_LABELS)
        self.assertIn('accuracy', metric)
        self.assertIn('f1_score', metric)
