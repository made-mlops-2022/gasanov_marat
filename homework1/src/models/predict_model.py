import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline


def predict_model(model: GradientBoostingClassifier, test_features: pd.DataFrame) -> np.ndarray:
    predicted = model.predict(test_features)
    return predicted
