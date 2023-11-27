import random

#matris
matris = [[random.randint(-99, 99) for j in range(10)] for i in range(10)]
#j yatay i dikey
#toplam
yatay_toplam = max(sum(matris[i][j:j+3]) for i in range(10) for j in range(8))
dikey_toplam = min(sum(matris[i][j] for i in range(k, k+3)) for j in range(10) for k in range(8))

print(matris)
print("yatay MAX toplam:",yatay_toplam)
print("dikey MİN toplam:",dikey_toplam)
# max grup
yatay_grup = max(((matris[i][j:j+3]) for i in range(10) for j in range(8)), key=sum)
dikey_grup = min(((matris[i][j] for i in range(k, k+3)) for j in range(10) for k in range(8)), key=sum)

if abs(yatay_toplam) > abs(dikey_toplam):
    print("Melih kazandi.")
elif abs(dikey_toplam) > abs(yatay_toplam):
    print("Mübariz kazandi.")
else:
    print("Bugün temizlik yok .")

