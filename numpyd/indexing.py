import numpy as np

numbers  = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]#number of 6
result = numbers[-1]
result = numbers[:3]


numbers2  = np.array([[0,5,10],[15,20,25],[50,75,85]])

result = numbers2[0]#first array
result =numbers2[2,1]
result = numbers2[:,2]# 3rd numbers of all series
result = numbers2[:,0:2]
reuslt = numbers2[:2,:2]
print(result)

arr1 = np.arange(10)
arr2 = arr1#thier address are same
arr3 = arr1.copy()
arr2[0] = 20
print(arr1)#arr1 also changed