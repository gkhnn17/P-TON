#**********************BEAUTİFULSOUP*****************************
html_doc ="""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam</title>
</head>
<body>
    <h1 id="header"><!--etiket-->
        PYTHON KURSU
    </h1>
    <div class = "grup1"><!--grup-->
        <h2>
            Programlama
        </h2>
        <ul> <!--liste ekleme-->
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class = "grup2">
<h2>
            Moduller
        </h2>
        <ul> 
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
</body>
</html>



"""

from bs4 import BeautifulSoup

soup =BeautifulSoup(html_doc,"html.parser")#ayrıştırıcı

result =soup.prettify()
result = soup.title
result = soup.head.name
result = soup.title.string#titlesız içeriği
result = soup.h2.string

result =soup.find_all("h2")[0]
result =soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()
result = soup.div.findNextSibling()

#print(link.get("href"))

print(result)