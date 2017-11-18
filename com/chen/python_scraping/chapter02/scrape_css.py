from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"html.parser")

nameList2 = bsObj.findAll("span",{"class":{"red","green"}})
for name in nameList2:
    print(name.get_text())

print('\n-- - -- - -- -- - -- - -- -- - -- - \n')


list3 = bsObj.findAll(id="text")
for obj in list3:
    print(obj)

print('\n-- - -- - -- -- - -- - -- -- - -- - \n')

list4 = bsObj.findAll(text= "The prince",limit=2)
for obj in list4:
    print(obj)



