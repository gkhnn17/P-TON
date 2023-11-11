import numpy as np

result = np.array([1,3,5,7,9])

result = np.arange(1,10)
result = np.arange(10,100,3)
result = np.zeros(10)
result = np.linspace(0,100,5)#5 eşitparçaya böl
result = np.random.randint(0,10)#random number
result = np.random.randint(0,10,3)# 3 pieces number

np_array =np.arange(50)
np_multi = np_array.reshape(5,10)#10 rows 5 columns
print(np_multi.sum(axis=1))#sum to 2. colums

rnd_number = np.random.randint(1,100,10)
result = rnd_number.argmax()#which number is the largest




print(result)