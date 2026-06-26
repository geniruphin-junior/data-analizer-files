import pandas as pd

"""df = pd.read_excel("buget.xlsx")



total = df.groupby("Produit")["Prix"]
print(total)





produit = total.sor

t_values(by="Prix", ascending=True)  # du plus petit au plus grand
print(total)





# df = df.isna()



value = int(
    input(


# print(df.describe())
    )
)



loc = df.iloc[4, 5]



cas = df.isna().sum()



    input(



        f" veux tu que vos cases vides >> \n {cas} soient remplacées, 

par quelle valeure par defaut : "
    )


)









jls_extract_var = print
jls_extract_var(df.sort_values("eleves", ascending=jls_extract_def()))
print(df.corr())


df.to_csv("correct.csv", index=False)"""

import matplotlib.pyplot as plt

bar = {
    "villes": ["cong", "cong", "likasi", "goma", "kisangani", "goma"],
    "eleves": [15, 37, 45, 356, 4, 7],
    "argent": [400, 340, 490, 456, 344, 456],
}

df = pd.DataFrame(bar)

print(df.value_counts("eleves"))
print(df.sort_values("eleves", ascending=False))
print(df.select_dtypes(exclude="str").corr())
plt.plot(df["eleves"], df["argent"], alpha=0.3, marker="o", color="#fff000")
plt.grid(True, linestyle="--", color="#00f0ff", alpha=0.3)
plt.xlabel("eleves", color="black")
plt.ylabel("argent", color="#00ff04")
plt.show()
