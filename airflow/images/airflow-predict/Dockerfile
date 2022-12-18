FROM airflow-ml-base:latest

COPY homework1/src/. ./src
COPY airflow/data/. ./data
COPY airflow/images/airflow-predict/predict.py /predict.py

ENTRYPOINT ["python", "predict.py"]