import json

person_string ='{"name": "ali", "languages": ["piton","seesharp"]}'
#json string on dict
"""
#result =json.loads(person_string)
#result = result["name"]

with open("person.json") as f:
    data = json.load(f)
    print(data["name"])
    print(data["languages"])
"""
person_dict = {
    "name": "Ali",
    "languages": ["Python", " C#"]
}
"""
#dict to string
result = json.dumps(person_dict)#string bilgiye çevirir

with open("person.json","w") as w:
    json.dump(person_dict,w)
"""

person_dict =json.loads(person_string)

result =json.dumps(person_dict , indent = 4 ,sort_keys = True)
print(person_dict)
print(result)