from matplotlib import pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
ali = [10, 15, 12, 20, 25, 22, 30]
vali = [8, 12, 18, 16, 22, 27, 28]

plt.plot(kunlar, ali, label="Ali", marker="o", color="gray")
plt.plot(kunlar, vali, label="Vali", color="red", marker="*")

plt.title("Ali and Vali")
plt.xlabel("Ali")
plt.xlabel("Vali")

plt.legend()
plt.grid(True)
plt.show()