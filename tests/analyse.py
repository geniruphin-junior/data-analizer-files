import pandas as pd
import sys

df = pd.read_csv("bonus.csv")

data_clean = df.dropna()
