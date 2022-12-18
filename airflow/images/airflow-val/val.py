import os
import pickle
import click
import pandas as pd
import src.data as data
import src.models as models
import src.entities as entities


@click.command("val")
@click.argument("input_model_path")
@click.argument('input_dir')
@click.argument('output_metric_path')
def val(input_model_path, input_dir, output_metric_path):
    test_features, test_target = pd.read_csv(f'{input_dir}/test_features.csv'), \
                                 pd.read_csv(f'{input_dir}/test_target.csv')
    with open(input_model_path, 'rb') as f:
        model = pickle.load(f)
    predicted = models.predict_model(model, test_features)
    os.makedirs(output_metric_path, exist_ok=True)
    metrics = models.serialize_metric(predicted, test_target['condition'], f'{output_metric_path}/metrics.json')


if __name__ == '__main__':
    val()
