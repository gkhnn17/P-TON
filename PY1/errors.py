#**************ERROR*************#
while True:
    try:
        x = int(input("x:"))
        y = int(input("y:"))
        print(x/y)
    except (ZeroDivisionError , ValueError) as e:
        print("Give right numbers")
        print(e)
    except Exception:#Genel error
        print("what did yo do",Exception)
    else: #doğru girilene kadar sorar
        print("code working completely")
        break
    finally:
        print("try is finished")
