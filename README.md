# Экзаменационный проект

### Задание 1:
Документ [постановка цели](purpose.md)

### Задание 2:
[Манифест](manifest.md)

### Задание 3:

Из корня проекта необходимо запустить:

```bash
docker compose -f infrastructure/docker-compose.yml up -d --build
```

Проверка запущенных контейнеров:

```bash
docker ps
```
Все контейнеры должны быть healthy:

![alt text](<screenshots/containters healthy.JPG>)

Запускаем эксперимент в MLFlow

```bash
docker exec -it ml_api python -u -m app.train
```

Эксперимент отображается в ui:

![alt text](<screenshots/experiment mlflow.png>)

Внутри контейнера airflow необходимо создать пользователя:

```bash
docker exec -it airflow_webserver bash
```

```bash
airflow users create \
  --username YOUR_USERNAME \
  --password YOUR_PASSWORD \
  --firstname YOUR_FIRSTNAME \
  --lastname YOUR_LASTNAME \
  --role Admin \
  --email admin@example.com
```

После логина будет виден пайплайн. Пайплайн успешно запускается.

![alt text](<screenshots/airflow pipeline success.png>)

### Задание 4

Документ [SLI / SLO](sli_slo.md)

### Задание 5

Исследование latency [Jupyter Notebook](latency_analysis/latency_analysis.ipynb)

ADR документ: [001_latency_improvement](docs/adr/001_latency_improvement.md)