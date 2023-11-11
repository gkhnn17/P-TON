#iSTENEN HİSSE BİLGİSİ ALINIR :)
#ALINAN HİSSELER KAYDEDİLİR   :)
#BAŞLATILDIĞINDA HİSSENİN O ANKİ DURUMUYLA İLGİLİ BİLGİLER ALINIR :)
#arayüze try excep ile işlem yapılacak :)
#aynı birimler alt alta gelecek şekilde yerleştirilecek       -yeni row ile bigiler güncellencek - öncesinde aynı unit varmı diye de kontrol edilecek
#selling bulunacak
import requests
from bs4 import BeautifulSoup
from datetime import date
from sqlite3 import connect

#https://uzmanpara.milliyet.com.tr/borsa/hisse-senetleri/pasifik-gmyo-psgyo/
#https://uzmanpara.milliyet.com.tr/borsa/hisse-senetleri/anadolu-efes-aefes/
class Borsa:
    def __init__(self):
        #self.hisse = hisse
        self.url = "https://uzmanpara.milliyet.com.tr/canli-borsa/"
        html = requests.get(url=self.url).content
        self.soup = BeautifulSoup(html,"html.parser")

        #DB 
        self.connection = connect("Share.db")
        self.mycursor = self.connection.cursor()


        #Today
        self.today = date.today()
        self.day = self.today.day
        self.month = self.today.month
        self.currentime = f"{self.day:02d}-{self.month:02d}"  # Create a string in "dd-mm" format

    


        self.arayüz()


        

    def arayüz(self):
        query = input("1-Hisse seç: 2-Tüm Durum gör:")
        
        if query =="1":
            while True:
                hisse = input("hisse:")

                if hisse =="X":
                    break
            
               #CHECK AND MAKİNG ID
                id_hisse = ("h_tr_id_"+hisse)
                id_buying_price = ("h_td_fiyat_id_"+hisse)
                
                buying_price = self.finding_buying_price(id_hisse,id_buying_price)
                selling_price = self.finding_selling_price(id_hisse)
                if buying_price is not None:
                    #PUTİNG İNPUTS İN Table
                    
                    try:
                        unit = int(input("How many did you took :"))
                    
                        self.mycursor.execute("INSERT INTO Shares(Name, Buying,Selling,Unit,Date) VALUES (?, ?, ? ,? , ?)",
                                        (hisse,buying_price,selling_price,unit,self.currentime))
                    
                        self.connection.commit()
                        print("Hisse kaydedildi")
                    except Exception as exp :
                        print("Your inputs have a problem")
                    
                else:
                    print(f"{hisse} is not founded.")
                #END OF Query
        
        
            self.arayüz()

        elif query =="2":
            self.printer(self.soup)

    #with SOUP
    def finding_buying_price(self,id_hisse,id_buying_price):
        try:
            #Geniş
            hisse = self.soup.find("tr",{"id":id_hisse})
            #dar
            buying_price = hisse.find("td",{"id":id_buying_price}).text.strip()
            return buying_price
        except Exception as err:
            print(f"Your item is not founded !")
            return None
        
    def finding_selling_price(self,id_hisse):
        hisse = self.soup.find("tr",{"id": id_hisse})
        link = hisse.find("a")
        href = link.get("href")
        url = requests.get("https://uzmanpara.milliyet.com.tr" + href).content
        sellsoup = BeautifulSoup(url,"html.parser")
        currency_cell = sellsoup.find_all("td",class_="currency")
        
        for cell in currency_cell:
            if cell.text.strip() == "Alış":
                value_cell = sellsoup.find("td",class_="right")
                sale_value = value_cell.text.strip()
                return sale_value
            

    def selecting(self):
        pass
        

    def printer(self,soup):
        #SELECTİNG
        self.mycursor.execute("SELECT * FROM Shares ORDER by Name")

        #FETCHİNG
        result = self.mycursor.fetchall()  
        
        #print
        for share in result:
            print(f"Name: {share[1]} ::, price:{share[2]}, Selling:{share[3]} Date:{share[5]}")
        self.connection.close()

b1 = Borsa()