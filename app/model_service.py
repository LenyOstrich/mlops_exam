import joblib
import pandas as pd


class DemandForecastService:
    def __init__(self, model_path: str, preprocessor_path: str):
        self.model = joblib.load(model_path)
        self.preprocessor = joblib.load(preprocessor_path)

    def predict(self, features: dict) -> float:
        df = pd.DataFrame([features])
        X = self.preprocessor.transform(df)
        return float(self.model.predict(X)[0])