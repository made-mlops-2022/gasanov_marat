import os.path
import sys

import pandas as pd

from human_model import HumanModel
import csv

# sys.path.append('../homework1/')
# sys.path.insert(1, '/../homework1')
sys.path[1] += '/../homework1'
import src

MODEL_PATH = '../homework1/models/model.pkl'


def query_predict(human_model: HumanModel):
    with open('predict.csv', 'w', encoding='UTF8', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(
            ['', 'age', 'sex', 'cp', 'trestbps', 'chol',
             'fbs', 'restecg', 'thalach', 'exang',
             'oldpeak', 'slope', 'ca', 'thal'])
        writer.writerow([0] + [item[1] for item in list(human_model)])
    csv_path = os.path.dirname(os.path.abspath(__file__)) + '/predict.csv'
    src.run_predict(MODEL_PATH, csv_path, 'predicted.csv')
    with open('predicted.csv') as f:
        return int(f.read()[5])
