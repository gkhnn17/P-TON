#*************************DECORATOR******************
"""
def my_decorator(func):
    def wrapper(name):#isim çağırmak için lazım
        print("fonksiyondan önceki")
        func(name)#foksiyonu burdan başlattırdık
        print("fonksiyondan sonraki işlemler")
    return wrapper

def hello(name):         
    print("hello",name)



hello = my_decorator(hello)

@my_decorator #greeting = my_decorator(greeting)
def Greeting():
    print("greeting")   

hello("gökhan")
Greeting("gökhan")
"""

""" OUTPUT
    ----->
    fonksiyondan önceki
    hello
    fonksiyondan sonraki işlemler
    <-----
"""
"""
import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):#değişken sayıda argüman alınır
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print("fonksiyon " +func.__name__+ str(finish-start)+ "saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):

    print(math.pow(a,b))


@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usalma(2,3)
faktoriyel(3)
"""