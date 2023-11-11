def check_password(psw):
    import re
    if len(psw) < 8 :
        raise Exception("parolla must be longer than 8.")
    elif not re.search("[a-z]",psw):
        raise Exception("paralo must be have small letter.")
    elif not re.search("[A-Z]",psw):
        raise Exception("paralo must be have big letter.")
    elif not re.search("[0-9]",psw):
        raise Exception("paralo must be have small letter.")
    elif re.search("\s",psw):
        raise Exception("Parola cant have a empty")
    else:
        print("Welcome")
    
password = "122_aefukuae"
try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("you can pass")

