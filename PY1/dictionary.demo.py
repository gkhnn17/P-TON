ogrenciler = {}
number = input("öğrenci no :")
name =input("ögrenci adi :")


ogrenciler.update({
    number : {
    "ad ": name ,
    "phone" : number
    }
}
)
ogrno = input("no:")
ogrenci =ogrenciler[ogrno]
print(ogrenci)

print(f"no{ogrno} adi:{ogrenci['ad']}")