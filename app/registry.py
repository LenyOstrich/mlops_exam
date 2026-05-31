import mlflow


def register_model(run_id: str):
    model_uri = f"runs:/{run_id}/model"
    mlflow.register_model(model_uri, "DemandModel")