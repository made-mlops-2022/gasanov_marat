import numpy as np
import pandas as pd


def extract_target(data: pd.DataFrame, target_column: str) -> tuple[pd.DataFrame, pd.Series]:
    target = data[target_column]
    return data.drop(target_column, axis=1), target
