import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        "Nom": ["Jean", "Marie", "Paul", "Alice"],
        "Age": [15, 20, 17, 25],
        "Ville": ["Marie", "Goma", "Kin", "Bukavu"],
    }
)

print(df[(df["Age"] >= 18) & (df["Nom"].isin(["Marie", "Alice"]))])
plt.subplot(1, 2, 1)
plt.plot("Nom", "Age", color="black", marker="o", linestyle="--")
plt.xlabel("nom", color="red")
plt.ylabel("ages", color="blue")
plt.grid(True, linestyle="-.", alpha=0.1, color="#ff04f0")
plt.title("ages par rapport aux noms")
plt.subplot(1, 2, 2)
plt.scatter("Ville", "Age", marker="o", alpha=0.5, color="cyan")
plt.xlabel("villes", color="red")
plt.ylabel("ages", color="blue")
plt.title("ages pqr rapport aux villes")
plt.show()
