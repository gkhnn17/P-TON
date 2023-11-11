import pandas as pd     

customers = {
'CustomerId': [1,2,3,4],
'FirstName': ["Ahmet", "Ali", "Hasan", "Canan"],
'LastName': ["Yılmaz", "Korkmaz","Çelik","Toprak"]
} 
orders = {
'OrderId': [10,11,12,13],
'CustomerId': [1,2,5,7],
'OrderDate': [ '2010-07-04', '2010-08-04', '2010-07-07', '2012-07-04']
}

df_customer = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

result = pd.merge(df_customer,df_orders,how="inner")#just "commons"
result = pd.merge(df_customer,df_orders,how="left")#main data "customer" if they dont have order Nan
result = pd.merge(df_customer,df_orders,how="right")#main data "order"
result = pd.merge(df_customer,df_orders,how="cross")#"mix"
result = pd.merge(df_customer,df_orders,how="outer")#all result "merged"


customersA = {
'CustomerId': [1,2,3,4],
'FirstName': ["Ahmet", "Ali", "Hasan", "Canan"],
'LastName': ["Yılmaz", "Korkmaz","Çelik","Toprak"]
}
customersB = {
'CustomerId': [4,5,6,7],
'FirstName': ["Yağmur", "Çınar", "Cengiz", "Can"],
'LastName': ["Bilge", "Turan", "Yılmaz", "Turan"]
}

df_customerA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customerB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result = pd.concat([df_customerA,df_customerB])#merged
result = pd.concat([df_customerA,df_customerB],axis=1)#abreast merged

print(result)