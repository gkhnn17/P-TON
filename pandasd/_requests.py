#********************REQUESTS****************************
import requests#html
import json

result =requests.get("https://jsonplaceholder.typicode.com/users")

result =json.loads(result.text)#str to dict

for i in result: 
    print(i["name"])

print(result[0]["name"])

#response 200 = successed