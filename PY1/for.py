
'''
number =[1,2,3,4, 9]
#FOR
for num in number:
    print(f"sayilar{num}")

tuple =[(1,2),(3,4)]

for a,b in tuple :
    print(a,b)

d = {"k1":1, "k2":2}
for key,value in d.items :
    print(key ,value )
'''
'''
#3ün kati
sayilar =[1,3,5,7,9]
for i in sayilar:
    if i%3 ==0:
        print(i)

'''

'''
sehirler =["kocaeli","sivas","ağri","burdur"]
for sehir in sehirler:
    if (len(sehir)) <=5:
        print(sehir)
'''

urunler =[
    {"name":"samsung","price":"3000"},
    {"name":"iphone","price":"30000"}
]
toplam = 0

for urun in urunler:
    print(urun)
for urun in urunler:
    print(urun["price"])

for urun in urunler:
    fiyat =int(urun["price"])
    print(urun["price"])
    toplam += fiyat
print(toplam)
