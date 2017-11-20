import requests
from bs4 import BeautifulSoup

headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': '',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

play_url = 'http://music.163.com/playlist?id=317113395'
s = requests.session()

s = BeautifulSoup(s.get(play_url,headers = headers).content)
main = s.find('ul',{'class':'f-hide'})

for music in main.find_all('a'):
    print('{} : {}'.format(music.text, music['href']))
