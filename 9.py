
from matplotlib import pyplot as plt

yillar = [2007, 2010, 2013, 2016, 2019, 2022, 2025, 2026]
avlodlar = [2, 3, 4, 5, 6, 14, 17, 18]

plt.plot(yillar, avlodlar, color="darkred", marker="o", linewidth=2, linestyle=":")

plt.title("Apple iPhone rivojlanishi")
plt.xlabel("Yillar")
plt.ylabel("iPhone avlodi")

plt.grid(True)

plt.savefig("natija.png")
plt.show()
