from dataclasses import dataclass
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class Params:
    input_data_path: str
    output_model_path: str
    output_metric_path: str
    metric_path: str
    val_size: float
    target_column: str


TrainingPipelineParamsSchema = class_schema(Params)


def read_training_pipeline_params(path: str) -> Params:
    with open(path, "r") as input_stream:
        schema = TrainingPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
