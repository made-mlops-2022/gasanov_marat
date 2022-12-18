FROM airflow-ml-base:latest

COPY homework1/src/. ./src
COPY airflow/data/. ./data
COPY airflow/images/airflow-val/val.py /val.py

ENTRYPOINT ["python", "val.py"]