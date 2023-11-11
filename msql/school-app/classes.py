class Class:
    def __init__(self,id,name,teacherId):
        self.id = id
        self.name = name
        self.teacherId = teacherId


    @staticmethod
    def CreateClass(obj):
        list =[]

        for i in obj:
            list.append(Class(i[0],i[1],i))

        return list