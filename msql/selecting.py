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

def getProductInfo():
    connection =mysql.connector.connect(host="localhost", user="root", password="Mysql123",database="node-app")
    cursor =connection.cursor()
    ##
    sql = "SELECT COUNT(name) From Products WHERE price >2000"#COUNT kaç adet
    sql = "SELECT AVG(price) From Products WHERE price >2000"#AVERAGE ortalama
    sql = "SELECT SUM(price) From Products WHERE price >2000"#SUM 
    sql = "SELECT MIN(price) From Products WHERE price >2000"#MIN 
    sql = "SELECT name From Products WHERE price = (SELECT MAX(price) from Products)"
    ##
    cursor.execute(sql)#içerisinde samsung bulunan 
    
    result = cursor.fetchone()

    print(f"id: {result[0]} ")

def getProducts():
    connection =mysql.connector.connect(host="localhost", user="root", password="Mysql123",database="node-app")
    cursor =connection.cursor()
    
    
    #sql = "SELECT * From Products ORDER By id "
    #sql = "SELECT *from categories"
    #sql = "SELECT * from Products inner join categories on categories.id=Products.categoryId"
    sql = "SELECT products.name,products.price,categories.name From products inner join categories on categories.id=Products.categoryId "#left-right...
    cursor.execute(sql)#DESC ->descent azalan ,ASC->ascent ->yükselen
    
    try:
        result = cursor.fetchall()
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print("Hata:",err)
    finally:
        connection.close()
        print("database kapandi")

def uptadeProduct(id,name,price):
    connection = mysql.connector.connect(host = "localhost", user = "root", password ="Mysql123",database="node-app")
    cursor = connection.cursor()

    #UPTADE
    sql = "UPDATE products SET name =%s,price =%s WHERE id = %s"
    values = name,price,id
    cursor.execute(sql,values)

    try:
        connection.commit()#güncelleme
        print(f"{cursor.rowcount} tane kayıt güncellendi")
        print(f"son eklenen kaydın id:{cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database kapandı.")

def deleteProduct(id):
    connection = mysql.connector.connect(host = "localhost", user = "root", password ="Mysql123",database="node-app")
    cursor = connection.cursor()

    #DELETE
    sql = "DELETE from products WHERE id=%s"
    values =(id,)
    cursor.execute(sql,values)
    try:
        connection.commit()#güncelleme
        print(f"{cursor.rowcount} tane kayıt silindi")
        print(f"son eklenen kaydın id:{cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database kapandı.")

getProducts()






"""def getProductById(id):
    connection =mysql.connector.connect(host="localhost", user="root", password="Mysql123",database="node-app")
    cursor =connection.cursor()


    sql = "SELECT * From Products Where id =%s"
    params = (id,)

    cursor.execute(sql,params)#içerisinde samsung bulunan 
    
    result = cursor.fetchone()

    print(f"id: {result[0]} Name : {result[1]}, price: {result[2]}")

getProductById(1)"""

"""def getProducts():
    connection =mysql.connector.connect(host="localhost", user="root", password="Mysql123",database="node-app")
    cursor =connection.cursor()

    #cursor.execute("SELECT *From Products")# * ->ile bütün kolonlar seçilir
    cursor.execute("SELECT name,price From Products WHERE id= 1")
    
    #FETCH
    result = cursor.fetchall()#fetch -> gidip getirmek birden fazla kayıt almak 
    #result =cursor.fetchone()

    for product in result:
        #print(f"Name :{product[1]}, price: {product[2]}")# * ile yapılanda 1. indeks
        print(f"Name : {product[0]}, price: {product[1]}")# name ve price 'select'lenen

"""
