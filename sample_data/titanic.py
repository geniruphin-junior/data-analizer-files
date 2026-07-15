import pandas as pd
import numpy as np
import plotly.express as px
import os

try:
    file = "titanic.csv"
    df = pd.read_csv(file)
    df["argent"] = np.random.randint(200, 900, 891)
    df = df.dropna()
    group = df.groupby("Sex")["Age"].agg(
        {
            "maximum": max,
            "minimum": min,
            "total": sum,
            "moyenne": np.mean(),
        }
    )
    print(group)
except FileNotFoundError:
    print("chemin introuvable")
