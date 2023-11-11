#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

import requests

class Github :
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "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"
 
    def getUSer(self,username):
        response =requests.get(self.api_url + "/users/" + username)
        return response.json()

    def getRepositories(self,username):
        response =requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()


    def createRepository(self,name):
        response =requests.post(self.api_url+"/user/repos?acces_token"+self.token,json =
        {
            "id": 1296269,
            "name" : name,
            "description" : "first",
            "homepage": "https://github.com",
            
        })
        return response.json()
github = Github()

while True:
    secim = input("1 - Find User\n2 - Get Repository\n3 - Create Repository\n4 - Exit\n Seçim:")

    if secim == "4":
        break
    else:
        if secim == "1":
            username = input("username:")
            result = github.getUSer(username)
            print(f"name : {result['name']} public repos : {result['public_repos']} follower : {result['followers']}")

        elif secim == "2":
            username = input("username:")
            result = github.getRepositories(username)

            for repo in result:
                print(repo["name"])  

        elif secim == "3":
            name =input("repository name :")
            result = github.createRepository(name)
            print(result)
        else:
            print("yanliş secim")