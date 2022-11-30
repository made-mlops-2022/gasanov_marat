import os
from datetime import timedelta

from airflow import DAG
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
        "train_model",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(5),
) as dag:
    split = DockerOperator(
        image="airflow-split",
        command="/data/raw/{{ ds }} /data/split/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        mount_tmp_dir=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        mounts=[Mount(source="/Users/maratgasanov/ml_vk/2semestr/MLOps/airflow/data/", target="/data", type='bind')]
    )

    preprocess = DockerOperator(
        image="airflow-preprocess",
        command="/data/split/{{ ds }} /data/preprocess/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        mount_tmp_dir=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        mounts=[Mount(source="/Users/maratgasanov/ml_vk/2semestr/MLOps/airflow/data/", target="/data", type='bind')]
    )

    train = DockerOperator(
        image="airflow-train",
        command="/data/preprocess/{{ ds }} /data/model/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        mount_tmp_dir=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        mounts=[Mount(source="/Users/maratgasanov/ml_vk/2semestr/MLOps/airflow/data/", target="/data", type='bind')]
    )

    val = DockerOperator(
        image="airflow-val",
        command="/data/model/{{ ds }}/model.pkl /data/preprocess/{{ ds }} /data/metrics/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-val",
        do_xcom_push=False,
        mount_tmp_dir=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        mounts=[Mount(source="/Users/maratgasanov/ml_vk/2semestr/MLOps/airflow/data/", target="/data", type='bind')]
    )

    split >> preprocess >> train >> val
