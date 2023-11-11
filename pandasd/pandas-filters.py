import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

result = df.columns
result = df.head(5)#top 5
result = df.tail(1)#last 5
result = df[["Column1","Column2"]].head(5)
result = df[5:15][["Column1","Column2"]]

result = df >50 
result = df[df>50]
result = df[df["Column1"] > 50][["Column1","Column2"]]
result = df[(df["Column2"]>50) & (df["Column1"] <=70)][["Column1","Column2"]]

result = df.query("Column1 >=50 & Column1 %2==0")

print(df)
print(result)       