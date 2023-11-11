class Teacher:
    def __init__(self,id,branch,number,name,surname,birthdate,gender,classId):
        if id is None:
            self.id = 0
        else:
            self.id= id
        self.branch = branch
        self.name = name
        self. surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classId=classId