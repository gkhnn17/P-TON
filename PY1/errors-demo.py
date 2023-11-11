#integer test
liste = ["1","2","5a","dasf"]
for i in (liste):
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue

#input integer test
while True:
    deger = input("give me rent:")
    if deger == "q" :
        print("you are fired")
        break
    try:
        result = float(deger)
    except ValueError:
        print("hm")
        continue



def faktoriyel(x) :
    x= int(x)
    if x < 0:
        raise ValueError("negatif deger")

    result = 1
    for i in range(1,x+1):
        result *=i

    return result

for x in [5,10,20,-3,"ehe"]:
    try:
        y =faktoriyel(x)
    except ValueError(x) as err:
        print(err)
        continue
    print(y)

