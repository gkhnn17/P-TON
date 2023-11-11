#Methods
#*******CLASS*********
'''
class Person:
    adress = " no information"
    def __init__(this,name,year):#this anlamı p1 temsil ediyor hangi özellilker se sonrasında gelenler
        #object attributes
        this.name = name
        this.year = year
        print("init is working ")
    #instance methods
    def intro(this):
        print("hello there "+ this.name)

    def calculateAge(this):
        return 2019 - this.year

p1 = Person("ali",1990)
p2 = Person("buse",1991)
p1.intro()
p2.intro()

print(f"i am {p1.name} {p1.calculateAge()}")

'''

class Circle :
    #Class object attribute 
    pi = 3.14 
    
    def __init__(self,radius=1) :#belirtilmesse 1
        self.radius = radius

    #methods
    def perimeter_calculation(self):
        return 2*self.pi * self.radius
    
    def area_calculation(self):
        return self.pi * (self.radius**2)
    
c1 = Circle(2)
c2 = Circle(3)

print(f"c1 alan = {c1.area_calculation()} perimeter = {c1.perimeter_calculation()}")
        