import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

result = numbers1 +numbers2#it sum numbers in order
result = numbers1 + 10


mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

result = np.vstack((mnumbers1 ,mnumbers2))#mnumber is get to bottom of mnumbers1
result = np.hstack((mnumbers1 ,mnumbers2))#line up side by side

result =numbers1 >=5 #check to numbers are bigger than 5

print(numbers1[result])#it rewrite arrays true ones


print(result)
