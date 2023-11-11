#*******************************re module********************************
import re

#regular experssion

str ="Python kursundayiz şimdi sonra görüşür.Python.."

result = re.findall("Python",str)
result = len(result)

result = re.split(" ",str)#boşluk karakterlerinden böler

result = re.sub(" ", "-",str)#sub string boşuk ile - 'yi değiştirir

result = re.search("Python",str)#match
#result = result.span()#kaçıncı index
#result = result.start()
#result = result.group()#Python

result = re.findall("[abc]",str)#her karateri arar
result = re.findall("[a-c]",str)#a dan c ye
result = re.findall("[^abc]",str)#abc harici tüm karakterler

result = re.findall("[...]",str)#3 bas 
result = re.findall("^P",str)#P ile başlayan var mı ?
result = re.findall("$a",str)#a ile bitiyor mu ?S





print(result)

