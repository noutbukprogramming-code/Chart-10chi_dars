
from matplotlib import pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat, ball, color="green",   linestyle=":")

plt.xlabel("Tayyorlanish vaqti (soat)")
plt.ylabel("Test ballari")
plt.title("Tayyorlanish vaqti va test ballari bog'liqligi")

plt.grid(True)

plt.show()
