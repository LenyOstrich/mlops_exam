import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestRegressor
from app.data_preprocessor import DataPreprocessor


def train():
    #mlflow.set_tracking_uri("file:./mlflow_tracking")
    mlflow.set_experiment("demand_forecast")

    df = pd.DataFrame(
        {
            "price": [10, 12, 11, 13, 15, 16],
            "promo": [0, 1, 0, 1, 0, 1],
            "demand": [100, 120, 110, 130, 150, 160],
        }
    )

    target = "demand"

    with mlflow.start_run():
        prep = DataPreprocessor()
        X = prep.fit_transform(df, target)
        y = df[target]

        model = RandomForestRegressor(n_estimators=50)
        model.fit(X, y)

        preds = model.predict(X)
        mae = abs(preds - y).mean()

        mlflow.log_metric("mae", mae)

        mlflow.sklearn.log_model(model, "model")

        joblib.dump(model, "models/model.pkl")
        joblib.dump(prep, "models/preprocessor.pkl")

        mlflow.log_artifact("models/model.pkl")


if __name__ == "__main__":
    train()
