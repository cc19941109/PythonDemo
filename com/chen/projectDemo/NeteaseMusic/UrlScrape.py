from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random

random.seed(datetime.datetime.now())

def getCount1(url_str):
    html = urlopen("http://music.163.com"+url_str)

    bsObj = BeautifulSoup(html,"html.parser")
    return bsObj.find("div",{"class":"m-info"}).findAll("span",{"id":"cnt_comment_count"})

def getCount2(url_str):
    html = urlopen("http://music.163.com"+url_str)

    bsObj = BeautifulSoup(html,"html.parser")
    return bsObj.find("div",{"class":"u-title u-title-1"}).findAll("span",{"id":"j-flag"})

counts = getCount2("/#/song?id=418603077")

for count in counts:
    print(count)




