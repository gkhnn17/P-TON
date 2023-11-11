accountA ={
    "name": "Gokhan",
    "countNo":"1234",
    "balance":3000,
    "ekHesap":2000
}
accountB ={
    "name": "Ali",
    "countNo":"3334",
    "balance":2000,
    "ekHesap":1000
}

def getMoney(account,amount):
    print(f"merhaba {account['name']}")

    if (account['balance'] >= amount) :
        account["balance"] -=amount
        print("you dont need ek hesap")
    else :
        total = account['balance'] + account["ekHesap"]

        if(total >=amount):
            ekHesapUse = input("do you want to use(E/H)")

            if(ekHesapUse=="E"):
                balance =account["balance"]

                print("al")
            else:
                print("nope")
        else:
            print("nope")
                


getMoney(accountA,4000)
getMoney(accountA,3000)
