def addition(a,b):
    return a +b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return(a*b)
def division(a,b):
    return(a/b)

def process(f1,f2,f3,f4,processname):
    if processname =="addition":
        print(f1(2,3))
    elif processname=="substraction":
        print(f2(5,3))
    #...
    else:
        print("unknown process")

process(addition,substraction,multiplication,division,"addition")