from dbmanager import DbManager
from student import Student
import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg="********\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci sİl-\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/C)"   
        while True:
            print(msg)
            islem = input("Secim: ")
            if islem == "1" :
                self.displayStudent()
            elif islem == "2" :
                self.addStudent()
            elif islem == "3" :
                self.editStudent()
            elif islem == "4" :
                pass
            elif islem == "5" :
                pass
            elif islem == "6" :
                pass
            elif islem == "7" :
                break
            else:
                print("yanlıs secim")

    def addStudent(self):
        self.displayClasses()

        classid = int(input("Hangi Sınıf: "))
        number = input("numara: ")
        name = input("name: ")
        surname = input("surname: ")
        year = int(input("year: "))
        month = int(input("month: "))
        day = int(input("day: "))
        birthdate = datetime.date(year,month,day)
        gender = input("cinsiyer(E/K: )")

        student = Student(None,number,name,surname,birthdate,gender,classid)

        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()

        for i in classes:
            print(f"{i.id} : {i.name}")
            
    def editStudent(self):

        classid = self.displayStudent()
        studentid = int(input("öğrenci id:"))

        student = self.db.getStudentById(studentid)

        print(student[0].name)
        
        student[0].name = input("name: ") or student[0].name
        student[0].surname = input("surname: ") or student[0].surname
        student[0].classid = input("classid: ") or student[0].classid

        self.db.editStudent(student[0])
    
    def deleteStudent(self):
        classid = self.displayStudent()
        studentid =int(input("öğrenci id: "))

        self.db.deleteStudent(studentid)

    def displayStudent(self):
        self.displayClasses()
        classid = int(input("Hangi sınıf :"))
        students = self.db.getStudentsByClassId(classid)

        print("Öğrenci listesi")
        for std in students:
            print(f"{std.id}-{std.name} {std.surname}")
            """
            for index,std in enumerate(students):
                print(f"{index+1}-{std.name} {std.surname}")
            """
        return classid
    
app = App()
app.initApp()