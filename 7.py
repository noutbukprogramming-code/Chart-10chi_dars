from matplotlib import pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar, guruh_a, color="gray", marker="*", linestyle="dashdot")
plt.plot(testlar, guruh_b, color="green", marker="o", linestyle=":")

plt.title("Test Natijalar")
plt.xlabel("Testlar")
plt.ylabel("Ballar")
plt.grid(True)

plt.legend()
plt.show()