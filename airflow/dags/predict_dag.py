import os
from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "predict",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:
    model_path = Variable.get("model_path")
    predict = DockerOperator(
        image="airflow-predict",
        command="%s /data/raw/{{ ds }}/to_predict.csv /data/predicted/{{ ds }}/predicted.csv" % model_path,
        network_mode="bridge",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        mount_tmp_dir=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        mounts=[Mount(source="/Users/maratgasanov/ml_vk/2semestr/MLOps/airflow/data/", target="/data", type='bind')]
    )

    predict
