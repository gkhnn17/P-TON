"""
#LİST COMPREHENSİONS
numbers = [x**2 for x in range(10) if x%2]

years =[1900,2000,2010]
ages = {2023 - year for year in years}
print(ages)

numbers = [x if x % 2 ==0 else "tek" for x in range(10) ]
print(numbers)

numbers=[(x,y) for x in range(3) for y in range(3)]
"""
import random
print(random.randint(1,100))
sayi =10
for i in range(2,sayi):
        print(i)
