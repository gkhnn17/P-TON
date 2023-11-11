"""from bs4 import BeautifulSoup

with open("index.html","r") as file:
    doc = BeautifulSoup(file,"html.parser")

#print(doc.prettify)
tag = doc.title
tag.title = "hello" #change title

tag = doc.find_all("p")[0]


print(tag.string)
"""

