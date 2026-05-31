from datetime import datetime

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator


with DAG(
    dag_id="ml_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    train = DockerOperator(
        task_id="train",
        image="infrastructure-api:latest",
        command="python -m app.train",
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
    )

    evaluate = DockerOperator(
        task_id="evaluate",
        image="infrastructure-api:latest",
        command="python -m app.evaluate",
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
    )

    deploy = DockerOperator(
        task_id="deploy",
        image="infrastructure-api:latest",
        command="cp /app/models/model.pkl /app/models/production_model.pkl",
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
    )

    train >> evaluate >> deploy