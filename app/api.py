from fastapi import FastAPI
import joblib
import pandas as pd
import os
import joblib

if not os.path.exists("models/model.pkl"):
    raise RuntimeError("Model not found. Run training pipeline first.")

app = FastAPI()

model = joblib.load("models/model.pkl")
prep = joblib.load("models/preprocessor.pkl")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(features: dict):
    df = pd.DataFrame([features])
    X = prep.transform(df)
    return {"prediction": float(model.predict(X)[0])}
