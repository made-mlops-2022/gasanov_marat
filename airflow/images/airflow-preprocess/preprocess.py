import os
import pandas as pd
import src.data as data
import src.features as features
import click
import os


@click.command("preprocess")
@click.argument("input_dir")
@click.argument("output_dir")
def preprocess(input_dir: str, output_dir):
    train_dataset, test_dataset = data.read_csv_data(f'{input_dir}/train.csv'),\
                                  data.read_csv_data(f'{input_dir}/test.csv')
    train_features, train_target = features.extract_target(train_dataset, 'condition')
    test_features, test_target = features.extract_target(test_dataset, 'condition')

    os.makedirs(output_dir, exist_ok=True)
    train_features.to_csv(f'{output_dir}/train_features.csv')
    train_target.to_csv(f'{output_dir}/train_target.csv')

    test_features.to_csv(f'{output_dir}/test_features.csv')
    test_target.to_csv(f'{output_dir}/test_target.csv')


if __name__ == '__main__':
    preprocess()
