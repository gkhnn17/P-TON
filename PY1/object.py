def greeting(name):
    print('hello',name)

sayHello= greeting

#encapsulation

def outer(num1):
    print("outer")
    def inner_increment(num1):#dıştaki koddan ayrı 
        return num1 +1
    num2 = inner_increment(num1)#değer vermesek çalışmazdı
    print(num1,num2)
outer(10)


def factorial(number):
    if not isinstance(number,int):#o sınıfa ait olup olmadığı kontrol edilir
        raise TypeError("number must be an integer")
    
    if not number >= 0 :
        raise ValueError("number must be bigger than zero")
    
    def inner_factorial(number):
        if number <=1 :
            return 1
        
        return number* inner_factorial(number -1)
    
    return inner_factorial(number)

try:
    print(factorial("q"))
except Exception as ex :
    print(ex)