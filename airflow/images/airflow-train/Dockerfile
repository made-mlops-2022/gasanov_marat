FROM airflow-ml-base:latest

COPY homework1/src/. ./src
COPY airflow/data/. ./data
COPY airflow/images/airflow-train/train.py /train.py

ENTRYPOINT ["python", "train.py"]