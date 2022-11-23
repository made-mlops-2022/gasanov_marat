import json
import numpy as np


def make_json_examples(random_seed=1, number_examples=10):
    np.random.seed(random_seed)
    age = np.random.randint(20, 90, number_examples)  # age between 20 and 90
    sex = np.random.randint(0, 2, number_examples)  # sex 1-M 0-F
    cp = np.random.randint(0, 4, number_examples)  # cp: chest pain
    trestbps = np.random.randint(100, 150, number_examples)  # trestbps
    chol = np.random.randint(250, 350, number_examples)  # chol
    fbs = np.random.randint(0, 2, number_examples)  # fbs
    restecq = np.random.randint(0, 3, number_examples)  # restecg
    thalach = np.random.randint(100, 200, number_examples)  # thalach
    exang = np.random.randint(0, 2, number_examples)  # exang
    oldpeak = np.random.random(number_examples) + np.random.randint(0, 5, number_examples)  # oldpeak
    slope = np.random.randint(0, 3, number_examples)  # slope
    ca = np.random.randint(0, 4, number_examples)  # ca
    thal = np.random.randint(0, 3, number_examples)  # thal
    for i in range(number_examples):
        example_dict = {'age': int(age[i]),
                        'sex': int(sex[i]),
                        'cp': int(cp[i]),
                        'trestbps': int(trestbps[i]),
                        'chol': int(chol[i]),
                        'fbs': int(fbs[i]),
                        'restecg': int(restecq[i]),
                        'thalach': int(thalach[i]),
                        'exang': int(exang[i]),
                        'oldpeak': float(oldpeak[i]),
                        'slope': int(slope[i]),
                        'ca': int(ca[i]),
                        'thal': int(thal[i])
                        }
        with open(f'json_examples/example_{i}.json', 'w') as fp:
            json.dump(example_dict, fp)


if __name__ == '__main__':
    make_json_examples()
