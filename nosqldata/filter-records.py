import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb+srv://gokhand:wqWzQLrUvAvADmFT@atlascluster.tyzvfvv.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]


result = mycollection.find_one ({"_id": ObjectId("64e755614e6fb77e1e40988a")})

filter = {"name":"Samsung S5"}
for result in mycollection.find(filter):
    print(result)



result = mycollection.find({
    "name": {
        "$in" : ["Samsung S5","Samsung S6"]
    }
})
for i in result :
    print(i)

print("*********************")

result = mycollection.find({
    "price": {
        "$gte": 2000#greater than and equal
    }
})

for i in result :
    print(i)

print("*********************")

result = mycollection.find({
    "price": {
        "$eq": 2000# equal
    }
})

for i in result :
    print(i)

print("*********************")

result = mycollection.find({
    "price": {
        "$lte": 2000# less and equal
    }
})

for i in result :
    print(i)

print("*********************")

result = mycollection.find({
    "name": {"$regex": "^S"}#check it include S
})
