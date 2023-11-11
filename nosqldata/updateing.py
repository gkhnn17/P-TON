import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://gokhand:wqWzQLrUvAvADmFT@atlascluster.tyzvfvv.mongodb.net/node-app?retryWrites=true&w=majority")
mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)
"""
mycollection.update_one(
    {"name": "Samsung S6"},
    {"$set":{
        "name": "Iphone 7",
        "price": 5000
    }}
    )
"""
query = {"name": "Samsung S8"}

newvalues =     {"$set":{
        "name": "Iphone 8",
        "price": 7000
    }}
result = mycollection.update_many(query,newvalues)
print (f"{result.modified_count} number of records updated ")

for i in mycollection.find():
    print(i)