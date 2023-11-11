def exponentiation(number):

    def inner(power):
        return number**power
    
    return inner

two = exponentiation(2)
three = exponentiation(3)
print(two(3))#2**3
print(three(4))