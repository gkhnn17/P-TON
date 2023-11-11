import pandas as pd

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,5,7])

data = dict(apples = s1 , oranges = s2)
df = pd.DataFrame(data)

dF =pd.DataFrame([1,2,3,4])

list = [["AHmet",50], ["Ali", 60],["Yagmur",70]]
dF = pd.DataFrame(list,[1,2,3],["NAme","Grade"])

dict = {"Name": ["ahmet","ali","Yağmur"],"Grade":[50,60,70]}
dF = pd.DataFrame(dict,index = [231,232,233])

dict_list = [
    {"Name": "Ahmet","Grade":40},
    {"Name": "ali","Grade":50},
    {"Name": "yağmur","Grade":90}
            ]
dF = pd.DataFrame(dict_list,index=[231,232,233])


print(dF)