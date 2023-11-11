x = " global"

def function():
    x ="local "

function()
print(x)

name = "gok"
def changename(new_name):
    global name      # namenin değişikliği dışı da etkiler 
    name = new_name  # diğer türlü içerden ada dışardan gok olur
    print(name)

changename("ada")
print(name)

