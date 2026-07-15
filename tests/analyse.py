import pandas as pd
import sys

df = pd.read_csv("correct.csv")

data_clean = df.dropna()
