import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error


def evaluate():
    model = joblib.load("models/model.pkl")
    prep = joblib.load("models/preprocessor.pkl")

    df = pd.DataFrame({
        "price": [10, 12, 11],
        "promo": [0, 1, 0],
        "demand": [100, 120, 110]
    })

    X = prep.transform(df)
    y = df["demand"]

    preds = model.predict(X)

    return mean_absolute_error(y, preds)