import pymongo


#myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://gokhand:wqWzQLrUvAvADmFT@atlascluster.tyzvfvv.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

#result = mycollection.find_one()

#for result in mycollection.find({},{"_id":0,"price": 0}):#except id 
for result in mycollection.find({},{"_id":0,"name":1,"price":1}):#0->ı dont want 1->ı want
    print(result)