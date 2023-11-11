#Inheritance (kalıtım)

class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
        
        print("Person spawned")
    def who_am_i(self):
        print("PERSON")


class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.number = number
        print("Student Spawned")
    #override
    def who_am_i(self):
        print("i am student")

class Teacher(Person):
 pass
p1 = Person("ali","veli")
s1 = Student("gk","dmlp")

print(p1.firstName)
print(s1.firstName)
s1.who_am_i()