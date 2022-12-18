from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    loss: str = field(default="log_loss")
    learning_rate: float = field(default=0.1)
    n_estimators: int = field(default=100)
