import mysql.connector
from datetime import datetime
from connectioner import connection
from student import Student
from teacher import Teacher
from classes import Class

class DbManager:
    def __init__(self):
        self.connection = connection    
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        
        sql = "SELECT * FROM students WHERE id = %s"
        value = (id,)

        self.cursor.execute(sql,value)

        try:
            obj = self.cursor.fetchone()
            #return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("hata",err)

    def getClasses(self):
        sql = "SELECT * FROM class"

        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()#bütün öğrenci bilgisi
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Error: ",err)

    def getStudentsByClassId(self,classId):
              
        sql = "SELECT * FROM students WHERE ClassId = %s"
        value = (classId,)

        self.cursor.execute(sql,value)

        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
            #print(obj)
            #return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
        except mysql.connector.Error as err:
            print("hata",err)

    def addStudent(self,student :Student):
        sql = "INSERT INTO students(`Student Number`,Name,Surname,Birthdate,Gender,ClassId) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (student.number,student.name,student.surname,student.birthdate,student.gender,student.classId)

        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata",err)

    def editStudent(self,student: Student):
        sql = "UPDATE students SET `Student Number`=%s,Name=%s,Surname=%s,Birthdate=%s,Gender=%s,ClassId=%s WHERE id =%s"
        value = (student.number,student.name,student.surname,student.birthdate,student.gender,student.classId,student.id)

        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print("hata",err)

    def deleteStudent(self,studentid):
        sql = "DELETE FROM students WHERE id = %s"
        value = (studentid,)

        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi")
        except mysql.connector.Error as err:
            print("hata",err)

    def addTeacher(self,teacher: Teacher):
        pass

    def editTeacher(self,teacher: Teacher):
        pass

db = DbManager()


"""BEFORE THE LİST[]
student = db.getStudentById(3)
print(student.name)

student = db.getStudentsByClassId(1)
print(student.name)
"""
"""AFTER THE LİST[]
student = db.getStudentById(3)
print(student[0].name)#only [0]
student = db.getStudentsByClassId(1)
print(student[3].name)
"""
"""ADDSTUDENT
student = db.getStudentById(8)
student[0].name = "Mahmut"
student[0].surname="Tuncer"
student[0].number = "505"
db.addStudent(student[0])"""
"""
student = db.getStudentById(7)
student[0].name = "Polat"
student[0].surname="Alemdar"
db.editStudent(student[0])"""