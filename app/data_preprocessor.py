import pandas as pd


class DataPreprocessor:
    def __init__(self):
        self.feature_cols = None

    def fit(self, df: pd.DataFrame, target_col: str):
        self.feature_cols = [c for c in df.columns if c != target_col]

    def transform(self, df: pd.DataFrame):
        return df[self.feature_cols]

    def fit_transform(self, df: pd.DataFrame, target_col: str):
        self.fit(df, target_col)
        return self.transform(df)
