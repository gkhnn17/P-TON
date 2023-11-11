import json
import os

class User:
    def __init__(self,username,password,email) :
        self.username = username
        self.password = password
        self.email = email

class UserRepository :
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json",'r',encoding= "utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)#jsonı python yap
                    newUser = User(username = user["username"], password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users)

    def register(self,user : User):
        self.users.append(user)
        self.savetoFile()
        print("kullanici olusuturuldu")

    def login(self,username,password):
        
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("login yapildi")
                break
        
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Cikis yapildi.")

    def identity(self):
        if self.isLoggedIn:
            print(f"username:{self.currentUser.username}")
        else:
            print("giris yapilmadi")

    def savetoFile(self):
        #class to dict
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))#dumps dönüştürme

        with open("users.json", 'w') as file :
            json.dump(list , file)#dump ekleme 


repository = UserRepository()

while True :
    print("Menü".center(50,"*"))
    secim = input("1 - Register\n2 - Login \n3 - Logout\n4 - identitiy\n5 - Exit\seciminiz")
    if secim == "5":
        break
    else:
        if secim == "1":
            #register
            username = input("username : ")
            password = input("password : ")
            email = input("email : ")

            user = User(username = username , password=password , email= email)
            repository.register(user)

        elif secim == "2":
             #login
            if repository.isLoggedIn:
                print("zeten login")
            else:
                username = input("username:")
                password = input("password:")

                repository.login(username,password)
        elif secim == "3":
            repository.logout()

        elif secim == "4":
            repository.identity()
        else:
            print("yanlis secim")

