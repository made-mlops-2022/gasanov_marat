import click
import pandas as pd
import src.data as data
import src.models as models
import src.entities as entities
import os


@click.command("train")
@click.argument("input_dir")
@click.argument('output_model_path')
def train(input_dir, output_model_path):
    params = entities.TrainingParams(loss='exponential')
    train_features, train_target = pd.read_csv(f'{input_dir}/train_features.csv'), \
                                   pd.read_csv(f'{input_dir}/train_target.csv')
    model = models.train_model(train_features, train_target['condition'], params)
    os.makedirs(output_model_path, exist_ok=True)
    models.serialize_model(model, output_path=f'{output_model_path}/model.pkl')


if __name__ == '__main__':
    train()
