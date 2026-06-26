import matplotlib.pyplot as plt
import pandas as pd
import sys
import time

# mes listes prets à l'emploi
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 20, 15, 10, 5]

plt.suptitle("3 graphiques sur ma page", color="red")
plt.subplot(1, 4, 1)
plt.plot(x, y1, linestyle="-.", color="blue", alpha=0.2)
plt.title("courbe y1")

plt.subplot(1, 4, 2)
plt.plot(x, y2, color="red", linestyle="--", marker="o")
plt.title("courbe y2")

plt.subplot(1, 4, 3)
plt.bar(x, y1, edgecolor="black", color="cyan")
plt.title("subplot avec bar")
plt.grid(True, linestyle="--")

plt.subplot(1, 4, 4)
plt.hist(x, bins=4, color="#fff000", edgecolor="black")
plt.title("avec histograme")
plt.grid(True)

plt.show()
