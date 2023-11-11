import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3"])

df =df.reindex(["a","b","c","d","e","f","g","h"])

new_Column = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = new_Column
result = df

result = df.drop("column1",axis=1)#y axis
result = df.drop(["column1","column2"],axis=1)
result = df.drop("a",axis=0)

result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
#result= df["column1"].isnull().sum
result = df[df["column1"].notnull()]["column1"]

result = df.dropna()#if row has any Nan it delete this raw
result = df.dropna(axis=1)#if column has any Nan it delete this column

result = df.dropna(subset=["column1","column2"])#only search in  what include in 

#how ="all"
result = df.dropna(subset=["column1","column2"],how="all")#if all index are Nann its deleted
result = df.dropna(subset=["column1","column2"],how="any")#if it has any Nan its deleted
result = df.dropna(thresh = 2)#data at least  need 2 info

result =df.fillna(value="no input")#alter Nans

result = df.sum()
result = df.sum().sum()
result = df.size
result = df.isnull().sum()

def avarege(df):
    total = df.sum().sum()
    pieces = df.size - df.isnull().sum()
    return total/pieces

result = df.fillna(value = avarege(df))

print(result)                                                 