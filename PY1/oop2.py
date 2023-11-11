class Çalışan():
    kabiliyetleri = []
    unvanı = 'işçi'
    maaşı = 1500
    memleketi = ''
    doğum_tarihi = ''

print(Çalışan.maaşı)
print(Çalışan.memleketi)
print(Çalışan.doğum_tarihi)

Çalışan.isim = 'Ahmet'
Çalışan.yaş = 40

class Sipariş():
    firma = ''
    miktar = 0
    sipariş_tarihi = ''
    teslim_tarihi = ''
    stok_adedi = 0


jilet = Sipariş()
kalem = Sipariş()
pergel = Sipariş()
çikolata = Sipariş()

kalem = Sipariş()

kalem.firma
kalem.miktar
kalem.sipariş_tarihi
kalem.teslim_tarihi
kalem.stok_adedi

#Çünkü self.kabiliyetleri bir sınıf niteliği değil, bir örnek niteliğidir. Örnek niteliklerine erişebilmek için de ilgili sınıfı mutlaka örneklememiz gerekir.

"""
İşte self kelimesi, yukarıdaki kodda yer alan ahmet kelimesini temsil ediyor. Yani ahmet.kabiliyetleri şeklinde bir kod yazabilmemizi sağlayan şey, __init__() fonksiyonu içinde belirttiğimiz self kelimesidir. Eğer bu kelimeyi kullanmadan şöyle bir kod yazarsak:

class Çalışan():
    def __init__():
        kabiliyetleri = []
…artık aşağıdaki kodlar yardımıyla kabiliyetleri niteliğine erişemeyiz:

ahmet = Çalışan()
print(ahmet.kabiliyetleri)

"""
#self.isim = isim
#Bunu yapmamızın gerekçesi, isim parametresini sınıfımızın başka bölgelerinde de kullanabilmek. self kelimesini parametremizin başına yerleştirerek, bu parametreyi sınıfın başka yerlerinden de erişilebilir hale getiriyoruz.
# bir sınıf niteliği olan personel değişkenine nasıl eriştiğimize çok dikkat etmenizi istiyorum. Daha önce de söylediğimiz gibi, sınıf niteliklerine sınıf dışındayken örnekler üzerinden erişebiliyoruz. self kelimesi, bir sınıfın örneklerini temsil ettiği için, bir sınıf niteliğine sınıf içinden erişmemiz gerektiğinde self kelimesini kullanabiliriz.

class HarfSayacı:
    def __init__(self):
        #Bunların birer örnek niteliği olduğunu, başlarına getirdiğimiz self kelimesinden anlıyoruz. Çünkü bildiğiniz gibi, self kelimesi, ilgili sınıfın örneklerini temsil ediyor. Bir sınıf içinde örnek niteliklerine ve örnek metotlarına hep bu self kelimesi aracılığıyla erişiyoruz.
        self.sesli_harfler = 'aeıioöuü'
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
        self.sayaç_sesli = 0
        self.sayaç_sessiz = 0

    def kelime_sor(self):
        return input('Bir kelime girin: ')

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç_sesli += 1
            if self.sessizdir(harf):
                self.sayaç_sessiz += 1
        return (self.sayaç_sesli, self.sayaç_sessiz)

    def ekrana_bas(self):
        sesli, sessiz = self.artır()
        mesaj = "{} kelimesinde {} sesli {} sessiz harf var."
        print(mesaj.format(self.kelime, sesli, sessiz))

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayaç = HarfSayacı()
    sayaç.çalıştır()