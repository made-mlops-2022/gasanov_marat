import numpy as np
import pandas as pd
from entities import FeatureParams
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import Normalizer


def normalize() -> Pipeline:
    normalize_pipiline = Pipeline(
        [('normalizer', Normalizer(norm='l2'))]
    )
    return normalize_pipiline


def build_transformer(params: FeatureParams) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [
            (
                "normalizer",
                normalize(),
                params.normalize_features
            )
        ], remainder='passthrough'
    )
    return transformer


def extract_target(data: pd.DataFrame, target_column: str) -> tuple[pd.DataFrame, pd.Series]:
    target = data[target_column]
    return data.drop(target_column, axis=1), target
