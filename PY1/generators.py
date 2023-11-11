#**************************Generators*********************
"""
def cube ():
    result = []

    for i in range (5):
        result.append(i**3)# bellek üzerinde çok yer kalpşlar
    return result

print(cube())
"""

def cube():
    for i in range(2,5):
        yield i **3# bellkete yer kaplamaz ,saklanmaz

iterator =cube()

print((next(iterator)))
print((next(iterator)))

liste1 = [i**3 for i in range(5)]
listegnerator = (i**3 for i in range(5)) #normal parantez generator
print(liste1)
print(next(listegnerator))

