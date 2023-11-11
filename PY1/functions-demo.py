def infinite(*param):
    myList=[param]
    print(myList)

print(infinite(1,23,4,34,3,524,5))


def difisions(a):
    b = 1
    list =[]
    while not a == b :
        if (a% b==0) :
            list.append(b)
        b +=1
    print(list)
        
difisions(100)