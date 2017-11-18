from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

x = bsObj.findAll(lambda tag:len(tag.attrs)==2)

for obj in x :
    print(obj)
    print(obj.attrs)
    print()
