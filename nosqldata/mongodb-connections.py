import pymongo

#myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://gokhand:wqWzQLrUvAvADmFT@atlascluster.tyzvfvv.mongodb.net/node-app?retryWrites=true&w=majority")
mydb = myclient["node-app"]

mycollection = mydb["products"]


#print(mydb.list_collection_names())
#one
"""
product = {"name" :"Samsung S5", "price":2000}

result = mycollection.insert_one(product)

print(type(result))
print(result)
print(result.inserted_id)

"""
"""
#many
productList = [
    {"name" :"Samsung S9", "price":9000,},
    {"name" :"Samsung Sa", "price":10000,"cotegories":["telefon","elektronik"]},
    {"name" :"Samsung Sb", "price":11000,"description":"süper"}
]  

result = mycollection.insert_many(productList)
print(result.inserted_ids)
"""

