#********WHİLE*********#
'''
x =1 
while x <= 100 :
    print(x)
    x +=1
name =""
while not name.strip() :
    name = input("isminizi giriniz :")
print(f"hosgeldinzi{name}")
'''
'''
sayilar=[1,2,3,4,5]
i = 0 
while i < len(sayilar):
    print(sayilar[i])
    i +=1
'''
'''
head= int(input("enter head"))
final =int(input("enter final"))
while head <final:
    print(head)
    (head) += 1
'''
'''
i = 1
numbers =[]
while not i ==6:  
    number = (input(f"number{i}"))
    i +=1
    numbers.append(number)
print(sorted(numbers))
'''
#with dictionary products price list
x =0
products=[]
amount = int(input("how many product do you have"))
while x < amount  :
    name = input("name")
    price = input("price")
    products.append({
        "name": name,
        "price" : price
    })
    x += 1
for product in products :
    print(f"product name{name} price {price}")
print(products)
