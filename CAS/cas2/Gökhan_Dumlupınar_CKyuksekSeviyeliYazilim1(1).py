import pandas as pd

class User:
    def __init__(self, username, Id, Kod, Adet):
        self.username = username 
        self.Id = Id
        self.Kod = Kod
        self.Adet = Adet
        self.inventory = []#it is for stocks

    def enterence(self):
        while True:
            entered_username = input("Enter your username: ")
            if self.Members(entered_username):
                self.username = entered_username
                self.Stocks()
                self.shopping()
                break
            else:
                print("Username is not in the member list")

    def Stocks(self):
        product_list = [
            {"Kod": "201033", "İsim": "Arduino", "Adet": 12},
            {"Kod": "201034", "İsim": "STM32F303K8", "Adet": 4},
            {"Kod": "201040", "İsim": "Kamera", "Adet": 3},
            {"Kod": "201045", "İsim": "IMU", "Adet": 4}
        ]
        self.products = pd.DataFrame(product_list)
        print(self.products)

    def shopping(self):#selceting
        product_users = {}
        while True:
            entered_product = input("Select the product you want (Enter İsim): ")
            product_row = self.products.loc[self.products['İsim'] == entered_product]

            if not product_row.empty:
                product_name = product_row['İsim'].values[0]
                product_stock = product_row['Adet'].values[0]
                print(product_stock)

                if product_stock > 0:
                    self.inventory.append(product_name)
                    product_stock -= 1  # Decrease stock count by 1
                    print(product_stock)
                      # Update stock count in DataFrame                    
                    print(f"{product_name} added to your inventory.")
                    if product_name in product_users:
                        product_users[product_name].append(self.username)
                    else:
                        product_users[product_name] = [self.username]

                    print(f"Other users who selected {product_name}: {', '.join(product_users[product_name])}")
                else:
                    print(f"Sorry, {product_name} is out of stock.")
                
                self.Stocks()  # Display updated stock information
            else:
                print("Invalid product name. Please try again or enter 'exit' to finish shopping.")
                continue
            
            choice = input("Do you want to continue shopping? (Y/N): ")
            if choice.lower() == "n":
                break

    def Members(self, username):#member list
        members = pd.DataFrame([
            {"ID": "23000040", "İsim": "Burcu Özdemir"},
            {"ID": "22000025", "İsim": "Ebru Aydin"},
            {"ID": "23000027", "İsim": "Selim Arslan"},
            {"ID": "21000042", "İsim": "Mert Güneş"}
        ])
        return username in members["İsim"].values

user = User("", "", "", "")

while True:#it will ask user until exit
    entered_username = input("Enter your username (or 'exit' to quit): ")
    if entered_username.lower() == "exit":
        break

    if user.Members(entered_username):
        user.username = entered_username
        user.enterence()
        print("Username:", user.username)
    else:
        print("Username is not in the member list")

print("Goodbye!")