import pandas as pd 
import numpy as np

data = {
"Column1": [1,2,3,4,5],
"Column2": [10,20,13,45,20],
"Column3": ["abc", "bca","bade","cba", "dea"]
}
df = pd.DataFrame (data)

def kareal(x):
    return x*x
#lambda Notice that the anonymous function does not have a return keyword. This is because the anonymous function will automatically return the result of the expression in the function once it is executed.
kareal2 = lambda x: x*x

result =df
result = df["Column1"].unique()#just uniques
result = df["Column2"].nunique()#how many uniques that have
result = df["Column2"].value_counts()
result = df["Column1"]*2
result = df["Column1"].apply(kareal)
result = df["Column1"].apply(lambda x: x*x)
df["Column4"] = df["Column3"].apply(len)

result = df.sort_values("Column3")#arrange
print(result)

data = { 
    "Ay": ["Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran","Temmuz"],
    "Kategori": ["Elektronik", "Elektronik", "Elektronik", "Kitap", "Kitap", "Kitap","Kitap","Giyim","Giyim"],
    "Gelir": [20,30, 15, 14, 32, 42, 12, 36,52]
}
df = pd.DataFrame(data)
df = df.pivot_table(index="Ay",columns="Kategori",values="Gelir")#index y,columns x,values Gelir

print(df)

