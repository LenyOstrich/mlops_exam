FROM ghcr.io/mlflow/mlflow:v2.12.1

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2-binary