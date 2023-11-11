import numpy as np

result = np.array([10,15,30,45,60])                 #1
result = np.arange(5,15)                            #2
result = np.arange(50,100,5)                        #3
result = np.zeros(10)                               #4
result = np.random.randint(0,100,5)                 #5
result = np.linspace(0,100,5)                       #6
result = np.random.randint(10,30,5)                 #7
result = np.random.randn(10)                        #8
result = np.random.randint(10,50,15).reshape(3,5)   #9
matris = np.random.randint(10,50,15).reshape(3,5)   #10
print(matris)
"""rowTotal = matris.sum(axis = 1)
colTotal = matris.sum(axis=0)
print(rowTotal,colTotal)"""

result = matris.max()                               # 11
result = matris.mean()#ortalama
result = matris.argmax()                            # 12
arr = np.arange(10,20)
result = arr[0:3]                                   # 13
result = arr[::-1]                                  # 14
result = matris[0]                                  # 15
result = matris[1][2]                               # 16
result = matris[:,0]                                # 17
result = matris**2                                  # 18
cift = matris[matris%2 == 0]                        # 19
result = cift[cift > 0]





print(result)