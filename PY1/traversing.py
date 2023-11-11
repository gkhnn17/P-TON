with open("newfile.txt","r") as file :#file.close 'a gerek yok
    content =file.read()
    print(content)
    
    file.seek(0)#okuma konumunu taşır 
    print(file.tell())#konumunu söyler
    
    content2 =file.read(10)
    print(content2)