import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb+srv://gokhand:wqWzQLrUvAvADmFT@atlascluster.tyzvfvv.mongodb.net/node-app?retryWrites=true&w=majority")
mydb = myclient["node-app"]
mycollection = mydb["products"]

#result = mycollection.find().sort("name",1)#1 ->decrease,-1 -> increase
#result = mycollection.find().sort("price",-1)
result = mycollection.find().sort([("price",-1),("price",1)])
for i in result :
    print(i) 