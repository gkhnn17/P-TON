import mysql.connector

def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(host = "localhost", user = "root", password ="Mysql123",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,decription) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)


    cursor.execute(sql,values)#eleman işleme

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id:{cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database kapandı.")
      
def insertProducts(list):
    connection = mysql.connector.connect(host = "localhost", user = "root", password ="Mysql123",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,decription) VALUES (%s,%s,%s,%s)"
    values = list


    cursor.executemany(sql,values)#birden çok

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id:{cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database kapandı.")
list = []
while True:
    name = input("name of product :")
    price = float(input("price of product :"))
    imageUrl = input("image of product :")
    description = input("description of product :")
    list.append((name,price,imageUrl,description))
    result = input("devam ?")

    if result == "h":
        print("Kayitlariniz aktariliyor...")
        print(list)
        insertProducts(list)
        break

#insertProduct(name,price,imageUrl,description)