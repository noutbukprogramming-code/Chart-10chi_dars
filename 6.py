
from matplotlib import pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

plt.bar(mahsulotlar, sotuv, color="red")

plt.title("Do'konning bir haftalik savdosi")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotilgan mahsulotlar soni")

plt.show()

eng_kop = sotuv.index(max(sotuv))
eng_kam = sotuv.index(min(sotuv))

print("Eng ko'p sotilgan:", mahsulotlar[eng_kop], max(sotuv), "ta")
print("Eng kam sotilgan:", mahsulotlar[eng_kam], min(sotuv), "ta")
