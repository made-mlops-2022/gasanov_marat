import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import json


def evaluate_model(predicted_labels: np.ndarray, true_labels: pd.Series) -> dict[str: float]:
    return {'accuracy': accuracy_score(predicted_labels, true_labels),
            'f1_score': f1_score(predicted_labels, true_labels)}


def serialize_metric(predicted_labels: np.ndarray, true_labels: pd.Series, output_path) -> str:
    metrics_dict = evaluate_model(predicted_labels, true_labels)
    with open(output_path, 'w') as f:
        json.dump(metrics_dict, f)
    return output_path
