import requests

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
print(r.cookies)
print(r.text)

print(' -- - -- - - -- - -')

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')

url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)

r2 = requests.get('http://github.com', timeout=4)
# r2 = requests.get(url2,cookies=jar)
print(r2.history)
print(r2.raise_for_status())


