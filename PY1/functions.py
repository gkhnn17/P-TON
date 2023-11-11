#*************functions**************
def sayHello(name ="user"):#functions
    print("hello " + name)

sayHello("Gökhan")
sayHello()#user yazar


def whassup(name ="user"):
    '''
INput:...Output: explanations
print(help(whassup))
'''
    return "whassup " + name #msg

msg =whassup("Gökhan")
print(msg)


def total ( num1 , num2 ):
    return num1 + num2

result = total(10,20)
print(result)



def calculateage(born):
    return 2019 - born

agegokhan = calculateage(2017)
ageada =calculateage(2010)

print(ageada,agegokhan)
print(help(whassup))