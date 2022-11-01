import entities
import sys
import data
import features
import pickle
import models


def run_predict(model_path: str, input_data_path: str, output_data_path: str):
    dataframe = data.read_csv_data(input_data_path)
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    models.predict_to_csv(model, dataframe, output_data_path)


if __name__ == '__main__':
    run_predict(sys.argv[1], sys.argv[2], sys.argv[3])
