import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://gokhand:wqWzQLrUvAvADmFT@atlascluster.tyzvfvv.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)


print("*"*50)

#mycollection.delete_one({"name": "Samsung S6"})
result = mycollection.delete_many({})#regular expression
print(f"{result.deleted_count} records deleted")
for i in mycollection.find():
    print(i)

