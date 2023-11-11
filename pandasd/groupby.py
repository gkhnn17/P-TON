import pandas as pd
import numpy as np
personeller = {
'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan',"Rıza Ertürk","Mustafa Can"],
'Departman': ['İnsan Kaynaklari','Bilgi İşlem', 'Muhasebe','İnsan Kaynaklari','Bilgi İşlem','Muhasebe','Bilgi İşlem'],
'Yaş': [30,25,45,50,23,34,42],
'Semt': ['Kadiköy','Tuzla', 'Maltepe', 'Tuzla', 'Maltepe','Tuzla', 'Kadiköy'],
'Maaş': [5000, 3000, 4000, 3500, 2750, 6500,4500]
}

df = pd.DataFrame(personeller)


result = df["Maaş"].sum()
result = df.groupby("Departman").groups#get info
result = df.groupby(["Departman","Semt"]).groups


"""for name,group in df. groupby("Departman"):
    print(name)
    print(group)"""

result = df.groupby("Semt").get_group("Kadiköy")
result = df.groupby("Departman").sum()
result =df.groupby("Departman")["Maaş"].mean()
result = df.groupby("Semt")["Yaş"].count()
result =df.groupby("Departman").agg([np.sum,np.max])

print(df)
print(result)

