#************************************PANDAS*********************************

import pandas as pd
import numpy as np

#data
numbers = [20,30,40,50]
letters = [5,'b','c',9]
scalar = 5
dict = {'a': 10, 'b': 20, 'c': 30 , 'd': 40}


#pandas series
pandas_series = pd.Series(scalar,[0,1,2,3])
pandas_series = pd.Series(letters,['a','b','c','d'])# a - 5 ,b - b
pandas_series = pd.Series(dict)

pandas_series = pd.Series([20,30,40,50],['a','b','c','d'])
result = pandas_series[0]# = 20
result = pandas_series['a']# = 20
result = pandas_series.shape#(4,
result = pandas_series.sum()
result = pandas_series %2 == 0


print(pandas_series)
print(result)