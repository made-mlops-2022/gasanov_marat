import src.data as data
import click
import os


@click.command("split")
@click.argument("input_file")
@click.argument('output_dir')
def split(input_file, output_dir):
    dataset = data.read_csv_data(f'{input_file}/data.csv')
    train_dataset, test_dataset = data.split_data(dataset, 0.7)
    os.makedirs(output_dir, exist_ok=True)
    train_dataset.to_csv(f'{output_dir}/train.csv', index=False)
    train_dataset.to_csv(f'{output_dir}/test.csv', index=False)


if __name__ == '__main__':
    split()
