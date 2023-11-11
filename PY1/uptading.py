"""
with open("newfile.txt","r+") as file:#okuma + uptade
    print(file.read())

    file.write("deneme")
    """
"""
with open("newfile.txt","a") as file:
    file.write("\nemel")

with open("newfile.txt","r") as file :
    print(file.read())
"""
"""
with open("newfile.txt","r+") as file :
    content=file.read()
    content = " Efe Turan\n"+content
    print(content)
"""
with open("newfile.txt","r+") as file :
    list = file.readlines()
    file.writelines(list)
    print(list)