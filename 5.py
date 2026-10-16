from matplotlib import pyplot as plt

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

plt.plot(
    masofa,
    mashgulot,
    color="red",
    marker="o",
    linewidth=2.5,
    linestyle=":"
)

plt.xlabel("Mashg'ulotlar")
plt.ylabel("Masofa (km)")
plt.title("Sportchining yugurish masofasi")

plt.grid(True)
plt.show()

# 1--Sportchini yugurish masofasi birinchi mashg'ulotda 2km dan, oltinchi mashg'ulotdegi 6kmga oshgan.
# 2--Uchinchi mashg'ulotda masofa jichcha kamaygan, keyingi mashg'ulotlatda oshib keto'rgan.
