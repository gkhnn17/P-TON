import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,studentNumber,name,surname,birthdate,gender,id):
        if id is None:
            self.id = id= 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO students(`Student Number`,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)
                
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayit eklendi")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO students(`Student Number`,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)
                
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayit eklendi")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            Student.connection.close()

    @staticmethod
    def getInfo():
        sql = "SELECT COUNT(Name) from students WHERE Name LIKE '%an%'"
        Student.mycursor.execute(sql)

        try:
            result = Student.mycursor.fetchall()

            for student in result:
                print(student)

        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            Student.connection.close()
            
    @staticmethod
    def getStudentById(id):
        sql ="SELECT * from students where id = %s"
        value = (id,)

        Student.mycursor.execute(sql,value)
        
        try:
            obj =  Student.mycursor.fetchone()
            return Student(obj[1],obj[2],obj[3],obj[4],obj[5],obj[0])
        except mysql.connector.Error as err:
            print("Error",err)

    def uptadeStudent(self):
        sql = "UPDATE students set `Student Number` = %s,Name =%s,Surname =%s,Birthdate=%s,Gender=%s WHERE id=%s  "
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt")
        except mysql.connector.Error as err:
            print("HAta:",err)
        finally:
            Student.connection.close()
            
    @staticmethod
    def getStudentsGender(gender):
        sql ="SELECT * from students where gender = %s"
        value = (gender,)

        Student.mycursor.execute(sql,value)
        
        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("Error",err)

    @staticmethod
    def uptadeStudents(liste):
        sql = "UPDATE students set `Student Number` = %s,Name =%s,Surname =%s,Birthdate=%s,Gender=%s WHERE id=%s  "
        values = []

        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order ]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt")
        except mysql.connector.Error as err:
            print("HAta:",err)
        finally:
            Student.connection.close()

students =Student.getStudentsGender("E")
print(students)

liste = []
for std in students:
    std = list(std)#tuples are not alterable so first make it list
    std[2] = "Mr" + std[2]
    liste.append(std)

Student.uptadeStudents(liste)

"""
student = Student.getStudentById(8)

student.name="ÇINAR"
student.surname="turan"

student.uptadeStudent()
"""
        



"""ogrenciler = [
    ("301","Ahmet", "Yilmaz", datetime (2005, 5, 17), "E"),
    ("302", "Ali", "Can", datetime (2005, 6, 17),"E"),
    ("303","Canan", "Tan", datetime (2005, 7, 7), "K"),
    ("304", "Ayşe", "Taner", datetime (2005, 9, 23), "K"),
    ("305","Bahadir", "Toksöz", datetime (2004, 7, 27), "E"),
    ("306","Ali", "Cenk",datetime (2003, 8, 25), "E")
    ]
Student.saveStudents(ogrenciler)


ahmet = Student("308","hakan", "Yilmaz", datetime (2006, 10, 1), "E")
ahmet.saveStudent()
"""


