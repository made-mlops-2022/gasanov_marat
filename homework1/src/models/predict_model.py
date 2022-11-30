import os

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline


def predict_model(model: Pipeline, test_features: pd.DataFrame) -> np.ndarray:
    predicted = model.predict(test_features)
    return predicted


def predict_to_csv(model: Pipeline, test_features: pd.DataFrame, output_path: str) -> str:
    predicted = predict_model(model, test_features)
    os.makedirs(output_path[:output_path.rfind('/')], exist_ok=True)
    pd.DataFrame(predicted).to_csv(output_path)
    return output_path
