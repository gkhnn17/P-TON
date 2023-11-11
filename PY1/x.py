"""print("istanbul","bugün","yağmurlu",sep="-")#istanbul-bugün-yağmurlu
print("istanbul","bugün","yağmurlu",end="!")#istanbul bugün yağmurlu!
print(*"1234567")#elements separates -> 1 2 3 4 5 6 7"""
"""

Karakter dizisi \n ifadesi olduğu noktada yeni satıra geçer ve \n ve \r özel bir kaçış karakteri olduğu için yazılmaz örneğin 'D:\nevşehir\rock' 
bunu için 'D:\\nevşehir\\rock' yapılmalı yada print(r'D:\nevşehir\rock') 'eklenmeli'"""

"""print("abc" in "merhaba")#İN
print("abc" is "merhaba")#İS """

"""for i in range(2,100,*2):
    print(i)"""
"""
#break continue effects loops (while,for)
#contine ile pass arasındaki fark
for x in range(10) :
    if x == 5 :
        continue
        print("this sentences don't appear ")

    if x == 5 :
        pass
        print("this sentences is exist")#yani ikisinde de 5 yok 
         """ 
"""
liste = [1,2,3,4,5,6,7]
print(liste[5:2:-1])#reverse"""

#append : sona ekler
#instert :belirtilen konuma ekler
#remove : belirtilen elemanı siler
#del : belirtilen konumdakini siler
#pop : a = liste.pop(2) a = 2 olur ve listeden 2 çıkarılır
#index : elemanın indexi
#sort : küçükten büyüğe sırala
#count : elemanon kaç kez tekrar ettiği
#sum : topla


liste1 = [1,2,3,4,5,6]
liste2 = liste1 #bellek adresleri aynı yani liste2ye yapılan liste1 e yapılmıştır
"""
#TUPLES
#sadece okunabilir
demet = (1,2,3)
"""
"""# DİCTİONARY
sozluk = {"apple" : "elma","pen" : "kalem","big" : "büyük"}
sozluk["rose"] = "gül"
#del : elemanı sil
#clear : tümünü sil
print(sozluk["apple"])

#items() : reach keys and values
#keys() : only keys
#values() : only values
#uptade : yeni dict'i ekler
#copy : dict elemanlarını kopyalar """
"""
# SET#kümeler
kume = {1,2,3}
#remove : eleman çıkar
#add :eleman ekle
#difference : iki küme farkı  "-"
#intersection : kesişim kümesi "&"
#isdisjoint : ayrık kümeleler
#issubset : altkümesi mi 
#issuperset : üstkümesi mi
#union : birleşim "|"
"""
"""def topla(*sayilar):#sayısı belirsiz    
    sonuc = 0
    for i in sayilar:
        sonuc = sonuc + i
    return sonuc"""
"""
import math

#replace(old,new) 
#upper
#lower
#capitalize
#strip : it clear unneded spaces,or if you input things it delete  

"""
"""
import calendar
takvim = calendar.calendar(2017)
print(takvim)
"""
"""try:
    pass
except:
    pass
finally:
    pass
 
x = 99
if x >100:
    raise Exception("girilen sayı 100den fazla olamaz")

assert x ==100#it is like if raise if not x==100 raise exception ,x have to be 100

#dosya.open(r"file description",mode)
    #w : write
    #a : append
    #r : read
#dosya.close()"""
"""
sesli_harfler = "aeioü"
sayac = 0
kelime = input("kelime giriniz : ")

def seslidir(harf):
    print("sayac degiskeni : ",sayac)
    return harf in sesli_harfler

def artir():

    for harf in kelime:
        if seslidir(harf):
            sayac +=1   
    return sayac

print(f"{kelime},{sayac}")
"""
#global : her yerden ulasılabilir
            #  burda kelime ve sayac globaldir ancak kelimeyi değiştirme gibi bir amacımız yok
            #  pek önerilmez onun yerine
            #   global olmasa sondaki sonuc 0 dır


"""
sesli_harfler = "aeioü"
sayac = 0

def kelime_sor():
    return input("kelime giriniz :")

def seslidir(harf):
    return harf in sesli_harfler


def artir(sayac,kelime):
    for harf in kelime:
        if seslidir(harf):
            sayac +=1   
    return sayac

def ekrana_bas(kelime): 
    print(f"{kelime},{artir(sayac)}")

def calistir():
    kelime = (kelime_sor())


if __name__ == "__main__":#import edildiğinde direkt çalışmaz yalnız kendi main dosyasında direkt calışır
    calistir()
    #>>> sayac.seslidir('c')

"""

"""
#değişkenler :class attirbutes , "sınıf niteliği"
class Asker:
    kabiliyet =[]
    unvan = "subay"


Asker.isim = "Ahmet" #adding new feature
Asker.isim = "Murat"
print(Asker.kabiliyet)
print(Asker.unvan)
print(Asker.isim)# Murat
#Ancak tek kullanımlık yani tek bir asker oluşturlur
"""

"""
#Tek sınıftan,ortak özelliklere sahip üyeler  
class Asker:

    kabiliyet =[] #eklenen kabiliyetin tüm ögelere yansımasını istemezken
    personel_listesi = []#listenin her örneklemede büyümesini isteriz
    unvan = "subay"

Ahmet = Asker()#->instantiation ,"örnekleme"
Memet = Asker()
print(Ahmet.kabiliyet)
print(Ahmet.unvan)

"""
"""class Çalışan:
    selam = "merhaba"
    print(selam)
"""


"""
class Çalışan:
    kabiliyet = ["sınıf niteliği"]
    def __init__(self):
        self.kabiliyet =["üye niteliği"]#yalnız üyeye özel
    

Ahmet = Çalışan()
print(Ahmet.kabiliyet)#üye
print(Çalışan.kabiliyet)#sınıf
"""

"""
class Çalisan():
    personel = []

    def __init__(self,isim) -> None:
        self.isim = isim #isim i farklı yerde kullanılabilir yaptık
        self.kabiliyetler = []
        self.personel_ekle()
    def personel_ekle(self):
        self.personel.append(self.isim)#Çalisan.personel.append denilebilir 
        print(f'{self.isim} eklendi')

    @classmethod#decarotar #0 ken bile kullanma hakkı 
    def personel_sayisi(cls):
        print(len(cls.personel))
    @classmethod
    def personel_show(cls):
        print(f"{cls.isim} liste")
        for kişi in cls.personel:
            print(kişi)

    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetler.append(kabiliyet)

    def kabiliyet_show(self):
        print(f"{self.isim} bunlar: {self.kabiliyetler}")

"""
"""
class Sınıf():
    sınıf_niteliği = 0
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2
        self.örnek_niteliği = 0

    def örnek_metodu(self):
        self.örnek_niteliği +=1
        return self.örnek_niteliği
    
    @classmethod
    def sınıf_metodu(cls):#self de olurdu sadece bi gelenek
        cls.sınıf_niteliği +=1
        return cls.sınıf_niteliği 
    
        """

"""liste = [
    ("123", "A", "Alyazmalım", "akitap"),
    ("124", "B", "Baldudak", "bkitap"),
    ("125", "C", "Ceylangözlüm", "ckitap")
]

def bul(deger,sıra):
    return  [li for li in liste if deger ==li[sıra]]

def sorgula(ölcüt=None,deger=None):
    d ={
        "isbn": bul(deger,0),
        "yazar": bul(deger,1),        
        "eser": bul(deger,2),
        "yayınevi": bul(deger,3)
    }
    for öge in d.get(ölcüt,deger):
        print(*öge,sep=",")
"""
"""
class Entrance:
    def __init__(self,mesaj = "Müşteri no"):
        cevap = input(mesaj)
        print( "hi")

    @classmethod
    def paroladan(cls):
        mesaj = "lütfen parola"
        cls(mesaj)
    @classmethod
    def Tcden(cls):
        mesaj = "lütfen TC"
        cls(mesaj)
  

Entrance.paroladan()
"""
"""
class Mat():
    @staticmethod
    def karekok(sayi):
        return sayi **0.5
#örnek ve sınıf metotlaronon aksine ilk parametreleri self veya cls almıyor
#çünkü bu iki sınıfın veya örnek nitelikleriyle herhangi bir işi yok
"""
"""     
import time 
import random
import sys
class Oyuncu():
    def __init__(self,isim,can=5,enerji=100):
        self.isim = isim
        self.darbe = 0#oyuncuya air önceden bildirmeye gerek yok 
        self.can = can
        self.enerji = enerji

    def mevcut_durum(self):
        print("darbe: ",self.darbe)
        print("can",self.can)
        print("enerji", self.enerji)

    def saldır(self,rakip):
        print("Saldırı gerçekleştirildi")
        print("Saldırı sürüyor")
            
        for i in range(10):
            time.sleep(.3)
            print(".",end="",flush="True")

        sonuc = self.saldırı_sonucu()

        if sonuc == 0 :
            print("\nSonuç: kazanan yok")
            

        if sonuc == 1 :
            print("\nSonuç: rakip darbelendi")
            self.darbele(rakip)
            #rakip.darbele() darbelenen olmasa
        if sonuc == 2 :
            print("\nSonuç: rakip tarafından darbelendiniz")
            self.darbele(self)#self mevcut sınıf örneğini temsil eder
                                #kenimizeatıfta bulanacağımız zaman self

    def saldırı_sonucu(self) :
        return random.randint(0,2)

    def darbele(self,darbelenen):
        darbelenen.darbe +=1
        darbelenen.can -=1

        if (darbelenen.darbe %5 ) ==0 :
            darbelenen.can -=1
        if (darbelenen.can <1) :
            darbelenen.enerji= 0
            print(f"oyunu {self.isim} kazandı")
            self.oyundan_cık()

    def oyundan_cık(self):
        print("çıkıs")
        sys.exit()

siz = Oyuncu("Gökhan")
rakip = Oyuncu("Memet")

while True:
    print("Hamleler",
          "S",
          "k",
          "q",sep="\n")
    
    hamle = input("Hamle")
    if hamle == "s":
        siz.saldır(rakip)
        print("RAKİP ", rakip.mevcut_durum())

        print("SİZ ", siz.mevcut_durum())

        if hamle == "k":
            siz.kac()
        if hamle == "q":
            siz.oyundan_cık()
"""                
"""class Sınıf():
    __gizli ="gizli"

    def instance_method(self):
        print(self.__gizli)
        print("örnek method")

    @classmethod
    def class_method(cls):
        print("sınıf method")

    @staticmethod
    def static_method():
        print("statik method")

# __ bulananlar gizlidi sınıf içerisinden erişilrken dışından erişilemez """
"""

class Çalisan():

    __personel = []#ancak personel_show sayesinde görülebilir

    def __init__(self,isim) -> None:
        self.isim = isim
        self.kabiliyetler = []
        self.__personel_ekle()
    
    def __personel_ekle(self):
        self.__personel.append(self.isim)
        print(f'{self.isim} eklendi')
    #ayse adlı kullanıcı bile ayse.personel_ekle diyebilirdi


    @classmethod
    def personel_show(cls):
        print(f"{cls.isim} liste")
        for kişi in cls.__personel:
            print(kişi)

    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetler.append(kabiliyet)

    def kabiliyet_show(self):
        print(f"{self.isim} bunlar: {self.kabiliyetler}")
"""
'''Gizli üyeye erişmek
s = Çalisan("Mehmet")
s._Çalisan__personel_ekle()
'''

# _yarıgizli herhangi bir engeli yoktu sadece dışardan değiştirilmemesi gerektiği uyarılır

"""
class Program():
    def __init__(self):
        self.data = 0#nitelik
    
    
    def versiyon(self):
        return "0,1"
    
program = Program()
program.data = 1 #niteliğe ulaşım
program.versiyon()#metoda ulaşım





class Program():
    def __init__(self):
        self.veri = 0#nitelik
    
    @property#metodu niteliğe dönüştürmek
    def versiyon(self):
        return "0,1"
    
    #data yı veri yapmak istersek ama eski kodları bozmadan yapmanın yolu#backwardss compatibility
    @property#data metodunu nitelik gibi yaptık aynı çağrışımı yaptık
    def data(self):
        return self.veri
    
program = Program()
program.versiyon#nitelik gibi
program.veri
program.data
"""   """

class Program():
    def __init__(self):
        self._sayi = 1

    @property
    def sayi(self):
        print("alo")
        return self._sayi
    
    @sayi.setter#veri doğrulama kısıtlma
    def sayi(self,yenideger):
        if yenideger %2 == 0:
            self._sayi = yenideger
        else: 
            print("çiftdeğil")

        return self.sayi
    
p = Program()
p.sayi = 5
p.sayi =2
print(p.sayi)
"""



"""#Player taban sınıf ->birkaç sınıfta ortak bulunan nitelik ve metotları barındırır
#BASE CLASS-SUPER CLASS-PARENT CLASS   
class Player():
    def __init__(self,name,rank):
        super.__init__(name,rank)#diğer türlü herseferinde self.name 'i tanımlamamız gerekecekti 
        self.name = name
        self.rank = rank
        self.power = 0

    def move(self):
        print("ı like to moving moving")

    def get_point(self):
        print("points...")    

    def lose_point(self):
        print("losed :(")

class Soldier(Player):
    hometown = "Burdur"
    
    
    def __init__(self, name, rank):
        self.power= 100


    def move(self):
        print("rap rap rap")       
        return super().move()#ı like to moving moving
    
class Employee(Player):
    def __init__(self,*args):
        self.power= 100

class Boss(Player):
    def __init__(self, *args):
        self.power= 100

soldier1 = Soldier("Ahmet","Er")
soldier1.name
soldier1.move() 
"""

#TKİNTER
"""import tkinter as tk

window = tk.Tk()
window.geometry("200x70")

label= tk.Label(text="Merhaba zalim dünyA")
label.pack()

button = tk.Button(text="tamam",command=window.destroy)#destroy() yapmadık yapsak dokunmadan çalışırdı 
button.pack()

window.mainloop()   """
"""
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW",self.exit)

        self.label = tk.Label(text="merhaba tekrar")
        self.label.pack()

        self.button = tk.Button(text="Exit",command=self.exit)
        self.button.pack()

    def exit(self):
        self.label["text"] = "elveda"
        self.button["text"]= "wait"
        self.button["state"]= "disable" 
        self.after(2000,self.destroy)

window = Window()    
window.mainloop()  """
"""
def sayi (a):
    return a+20
print(sayi(10))
#lambda   
sayi = lambda a: a+20
print(sayi(10))
"""


liste = ["sari","yeşil","mor"]

myiter = iter(liste)
print(next(myiter))
print(next(myiter))
