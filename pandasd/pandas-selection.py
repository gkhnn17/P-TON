import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index = ["A","B","C "],columns=["Columns1","Columns2","Columns3"])

result = df
result = df["Columns1"]
result = df[["Columns1","Columns2"]]

#loc["row",column] , loc["row"] , loc[ : ,"column"]
result = df.loc[["A","B"],["Columns1","Columns2"]]
result = df.loc[:,"Columns1":"Columns3"]#result = df.loc[:,:"Columns3"]
result = df.iloc[1]#B 

df["Columns4"] = pd.Series(randn(3),["A","B","C"])
df["Columns5"] = pd.Series(randn(3),["A","B","C"])

df.drop("Columns5",axis=1)#delete but it doesn't modify the original DataFrame in-place by default.
df.drop("Columns5",axis=1 ,inplace=True)#delete

print(df)
print(result)