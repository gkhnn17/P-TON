import requests
import json

api_url=("https://api.freecurrencyapi.com/v1/latest?apikey=QSYUaOvalyNZHLqX7Qu3Euqd9zOQu4RIMWKafLj1")

bozulan_doviz =input("bozulan döviz turu:")#USD
alinan_doviz =input("alinan döviz turu:")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsun"))

result = requests.get(api_url)

result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_doviz,result["data"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2}".format(miktar, bozulan_doviz,miktar * result["data"][alinan_doviz]))