#******LAMBDA*******
#def square(num): return num**2

numbers =[1,2,3,9]


result = list(map(lambda num : num**2 ,numbers))#tek seferlik
'''
for item in map (square,numbers):
    print(item)
'''
print(result)


