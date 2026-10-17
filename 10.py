
from matplotlib import pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

bars = plt.bar(ismlar, ballar, color="darkred", linestyle=":")
plt.bar_label(bars)

plt.title("O'quvchilar test natijalari")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")
plt.grid(True)

eng_yuqori = max(ballar)
eng_past = min(ballar)
ortacha = sum(ballar) / len(ballar)


print(f"Eng yuqori ball olgan: {ismlar[ballar.index(eng_yuqori)]}-----bali--->{eng_yuqori}")

print(f"Eng past ball olgan: {ismlar[ballar.index(eng_past)]}-----bali--->{eng_past}")

print(f"O'rtacha ball: {round(ortacha, 2)}")

plt.savefig("oquvchilar_natijasi.png")
plt.show()
