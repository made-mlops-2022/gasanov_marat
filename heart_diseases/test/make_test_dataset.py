import numpy as np
import pandas as pd
import click


def make_dataframe(random_seed: int, number_elements: int, predict=False) -> pd.DataFrame:
    np.random.seed(random_seed)

    age = pd.Series(np.random.randint(20, 90, number_elements))  # age between 20 and 90
    sex = pd.Series(np.random.randint(0, 2, number_elements))  # sex 1-M 0-F
    cp = pd.Series(np.random.randint(0, 4, number_elements))  # cp: chest pain
    trestbps = pd.Series(np.random.randint(100, 150, number_elements))  # trestbps
    chol = pd.Series(np.random.randint(250, 350, number_elements))  # chol
    fbs = pd.Series(np.random.randint(0, 2, number_elements))  # fbs
    restecq = pd.Series(np.random.randint(0, 3, number_elements))  # restecg
    thalach = pd.Series(np.random.randint(100, 200, number_elements))  # thalach
    exang = pd.Series(np.random.randint(0, 2, number_elements))  # exang
    oldpeak = pd.Series(np.random.random(number_elements)+np.random.randint(0,5, number_elements))  # oldpeak
    slope = pd.Series(np.random.randint(0, 3, number_elements))  # slope
    ca = pd.Series(np.random.randint(0, 4, number_elements))  # ca
    thal = pd.Series(np.random.randint(0, 3, number_elements))  # thal
    condition = pd.Series(np.random.randint(0, 2, number_elements)) # condition

    df_dict = {
        'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol, 'fbs': fbs, 'restecg': restecq, 'thalach': thalach,
        'exang': exang, 'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal, 'condition': condition
    }
    if predict:
        del df_dict['condition']
    df = pd.DataFrame(df_dict)
    return df


def make_csv_dataset(random_seed: int, number_elements: int, output_path='out.csv', predict=False):
    make_dataframe(random_seed, number_elements, predict).to_csv(output_path)


if __name__ == '__main__':
    make_csv_dataset(1, 100, 'test/csv/test_train.csv')
    make_csv_dataset(1, 10, 'test/csv/test_predict.csv', predict=True)
