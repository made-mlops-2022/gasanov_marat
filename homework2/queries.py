import os.path
import sys
from human_model import HumanModel
import csv

# sys.path.append('../homework1/')
# sys.path.insert(1, '/../homework1')
sys.path[1] += '/../homework1'
print(sys.path)
import src

MODEL_PATH = '../homework1/models/model.pkl'


def query_predict(human_model: HumanModel):
    with open('predict.csv', 'w', encoding='UTF8', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(
            ['age', 'sex', 'cp', 'trestbps', 'chol',
             'fbs', 'restecg', 'thalach', 'exang',
             'oldpeak', 'slope', 'ca', 'thal'])
        print(human_model)
        writer.writerow([item[1] for item in list(human_model)])
        src.run_predict(MODEL_PATH, 'predict.csv', 'predicted.csv')
