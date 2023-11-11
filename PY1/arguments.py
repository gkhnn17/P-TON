def changeName(n):
    n = "ada"

name ="yiğit"
changeName(name)
print(name)

def change(n):
    n[0]="istanbl"

sehirler=["asdf","izmir"]
n = sehirler[:2]#slicing : sehirdeki bilgileri al-tou didn't touch original
n[0]="istanbl"#istanbl,izmir


print(sehirler)
print(n)

def add(*params):#a,b,c,d=10 ..gibi belirmeye gerek yok  #tuple
    return sum((params))

print(add(10,20))


def disPlayUser(**args):#using dictinionary
    for key,value in args.items():
        print(f"{key} is {value}")#name is gokhan,age is 2 ...

disPlayUser(name ="gökhan",age=2 ,city="london")
disPlayUser(name ="fatma",age=2 ,city="losangeles")


def myFunc(a,b,*args,**keywargs):
    print(a,b,args,keywargs)

myFunc(10,20,30,40,50, key1 ="value1",key2= "value2 ")