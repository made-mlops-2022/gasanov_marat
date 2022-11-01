import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
import pickle
from sklearn.pipeline import Pipeline
from entities import TrainingParams


def train_model(features: pd.DataFrame,
                labels: pd.Series,
                training_params: TrainingParams) -> GradientBoostingClassifier:
    model = GradientBoostingClassifier(loss=training_params.loss,
                                       learning_rate=training_params.learning_rate,
                                       n_estimators=training_params.n_estimators)
    model.fit(features, labels)
    return model


def create_inference_pipeline(
    model: GradientBoostingClassifier, transformer: ColumnTransformer
) -> Pipeline:
    return Pipeline([("feature_part", transformer), ("model_part", model)])


def serialize_model(model: object, output_path: str) -> str:
    with open(output_path, 'wb') as f:
        pickle.dump(model, f)
    return output_path
