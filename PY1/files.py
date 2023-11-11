"""
try:
    file = open("newfile.txt","r")
except FileNotFoundError:
    print("dosya okuma hatasi")
finally:
    print(file)
    """
"""
file =open("newfile.txt","r")
"""
"""
content =file.read()
print(content)

file.close()
"""

file =open("newfile.txt","r")
print(file.readline())
print(file.readline(),end="")
file =open("newfile.txt","r")
print(file.readlines())