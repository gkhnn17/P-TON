#*******CLASS*********
class Person:
    adress = " no information"
    def __init__(this,name,year):#this anlamı p1 temsil ediyor hangi özellilker se sonrasında gelenler
        #object attributes
        this.name = name
        this.year = year
        print("init is working ")



p1 = Person("ali",1990)
p2 = Person(name ="buse", year = 1991)
print(p1)

#Uptading
p1.adress = " Kocaeli"

print(f"name:{p1.name} year: {p1.year} adress : {p1.adress}")