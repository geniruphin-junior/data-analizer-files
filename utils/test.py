import pandas as pd

df = pd.read_csv("bonus.csv")
total = df.groupby("Produit")["Prix"].mean()

produit = total.sort_values(by="Prix", ascending=True)  # du plus petit au plus grand
print(produit)
