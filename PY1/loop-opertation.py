#RANGE
for item in range(2,100,2):#2 den 100 e +2
    print(item)

print(list(range(5,10)))

greeting = " hello"
#ENUMERATE
for item in enumerate(greeting):
    print(item)#(1, 'h') (2, 'e') (3, 'l')

for index ,letter in enumerate(greeting):
    print (f"index {index} letter {letter}")

#ZİP
list1 =[1,2,3,4]
list2= ["a","b","c","d"]

print(list(zip(list1,list2)))
