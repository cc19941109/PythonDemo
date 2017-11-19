from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


# random.seed方法的作用是给随机数对象一个种子值，用于产生随机序列。
# 对于同一个种子值的输入，之后产生的随机数序列也一样。
# 通常是把时间秒数等变化值作为种子值，达到每次运行产生的随机系列都不一样。-- 摘自百度

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while len(links)>0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)




