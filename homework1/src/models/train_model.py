import numpy
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import pickle


def train_model(features: pd.DataFrame, labels: pd.Series) -> GradientBoostingClassifier:
    model = GradientBoostingClassifier()
    model.fit(features, labels)
    return model


def serialize_model(model: object, output_path: str) -> str:
    with open(output_path, 'wb') as f:
        pickle.dump(model, f)
    return output_path
