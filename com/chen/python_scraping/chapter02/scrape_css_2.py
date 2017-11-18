from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"html.parser")


list1 = bsObj.findAll("span",{"class":"green"})

for obj in list1:
    print(obj.get_text())
