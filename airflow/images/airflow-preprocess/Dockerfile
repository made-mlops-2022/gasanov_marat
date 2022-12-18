FROM airflow-ml-base:latest

COPY homework1/src/. ./src
COPY airflow/data/. ./data
COPY airflow/images/airflow-preprocess/preprocess.py /preprocess.py

ENTRYPOINT ["python", "preprocess.py"]