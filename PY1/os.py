#**************************OS MODULE*************************
import os
import datetime

result =os.name#windows

os.chdir("..")#alt klasör
result = os.getcwd()#etkin klasör ismi
os.mkdir("newdirectory")#make diretory

os.makedirs("newdirectory/yeni")

result = os.listdir()#listeleme

for dosya in os.listdir():
    if dosya.endswith("py"):
        print(dosya)


result = os.stat("date.py")#dosya bilgisi

result = result.st_size/1024#kb
result = datetime.datetime.fromtimestamp(result.st_ctime)#created oluşturulma
result = datetime.datetime.fromtimestamp(result.st_mtime)#modified değiştirilme
result = datetime.datetime.fromtimestamp(result.st_atime)#acces son erişim tarihi

os.system("notepad.exe")#open notpad

os.rename("newdirectory","yeniklasör")

os.rmdir("newdirec")#remove

os.removedirs("yeniklasör/yeni")

#PATH

result = os.path.abspath("os.py")#show me the path

result = os.path.dirname("C:C:/Users/Casper/PİTON/os.py")#dizin kısmını döndürür
result =os.path.dirname(os.path.abspath("os.py"))
result = os.path.exists("os.py")#is it exist ?
result =(os.path.isdir)("C:/Users/Casper/PİTON")#is it directory ?
result =(os.path.isfile)("C:/Users/Casper/PİTON")#is it file ?
result = os.path.join("C:\\","DENEME")
result =os.path.split("C::\\deneme")


print(result)