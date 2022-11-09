from dataclasses import dataclass, field
from typing import List, Optional


@dataclass()
class FeatureParams:
    deleted_features: List[str]
    target_column: str
    normalize_features: List[str]
