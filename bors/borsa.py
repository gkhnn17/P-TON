#iSTENEN HİSSE BİLGİSİ ALINIR
#ALINAN HİSSELER KAYDEDİLİR 
#BAŞLATILDIĞINDA HİSSENİN O ANKİ DURUMUYLA İLGİLİ BİLGİLER ALINIR
import requests
from bs4 import BeautifulSoup
import json

class Borsa:
    def __init__(self):
        #self.hisse = hisse
        self.url = "https://uzmanpara.milliyet.com.tr/canli-borsa/"
        html = requests.get(url=self.url).content
        self.soup = BeautifulSoup(html,"html.parser")

        self.arayüz()


        

    def arayüz(self):
        query = input("1-Hisse seç: 2-Durum gör:")
        
        if query =="1":
            while True:
                self.hisse = input("hisse:")

                if self.hisse =="x":
                    break
                
                self.id = ("h_tr_id_"+self.hisse)
                self.idfiyat = ("h_td_fiyat_id_"+self.hisse) 
                
                data = {
                    "NAME": self.hisse,
                    "id" : self.id,
                    "idfiyat" : self.idfiyat
                    
                }

                with open("takiplistesi.json","a") as takiplistesi:
                    json_data = json.dumps(data)
                    takiplistesi.write(json_data + "\n")
                    takiplistesi.close()
            

                self.arayüz()

        elif query =="2":
            self.printer(self.soup)


    def printer(self,soup):
        id_data = []
        idfiyat_data = []
        with open("takiplistesi.json","r") as json_file:
            for line in json_file:
                data = json.loads(line)
                id = data.get("id")
                idfiyat = data.get("idfiyat")
                id_data.append(id)
                idfiyat_data.append(idfiyat)

        for i in range(len(id_data)):
            id = id_data[i]
            idfiyat = idfiyat_data[i]

            hisses = soup.find_all("tr",{"id":id})

            for hisse in hisses:
                hisse_fiyat = hisse.find("td",{"id":idfiyat}).text.strip()
                print(hisse_fiyat)


b1 = Borsa()


