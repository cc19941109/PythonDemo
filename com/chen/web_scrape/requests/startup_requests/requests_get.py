import requests

# r = requests.get('https://github.com/timeline.json',auth=('15355498770@163.com', '951846273cc'))
# print(r.raw)
# print(r.text)

payload = {'key1': 'value1', 'key2': ['value2','value3']}
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get("http://httpbin.org/get", params=payload,headers=headers)



# print(r.url)
# print(r.encoding)
# print(r.content)
print('- -- - - - -- ')
# print(r.text)

# print(r.json())

print(r.cookies)
print(r.status_code)
print(r.status_code==requests.codes.ok)
print(r.headers)
print(r.headers['content-type'])