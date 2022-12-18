FROM airflow-ml-base:latest

COPY homework1/src/. ./src
COPY airflow/data/. ./data
COPY airflow/images/airflow-split/split.py /split.py

ENTRYPOINT ["python", "split.py"]