from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import datetime
import random
import re

pages = set()
random.seed(datetime.datetime.now())


# 获取页面内所有的内链列表
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internalLinks = []
    # 找出所有以"/"开头的链接µ
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] not in pages:
            if link.attrs['href'] is not None:
                if (link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


def getInternalLinksByStr(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    return getInternalLinks(bsObj, url)


# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以 http/www开头欧且不包含当前 url 的链接
    for link in bsObj.findAll("a",href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def spiltAddress(address):
    addressParts = address.replace("http://","").spilt('/')
    return  addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks=getExternalLinks(bsObj,urlparse(startingPage).netloc)
    if len(externalLinks)==0:
        print("no external links , looking around the site for one")
        domain = urlparse(startingPage).scheme+ "://" + urlparse(startingPage).netloc
        print("scheme:"+urlparse(startingPage).scheme)
        print("urlparse(startingPage).netloc: "+urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bsObj,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("random external link is :"+externalLink)
    followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")



# x = getInternalLinksByStr("https://en.wikipedia.org")
# for xitem in x:
#     print(xitem)