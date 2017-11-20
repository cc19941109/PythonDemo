import requests
import json


url = "http://httpbin.org/post"
payload = {'some': 'data'}


# 两种方式的返回都一样
# r = requests.post(url, json=payload)
r = requests.post(url, data=json.dumps(payload))


print(r.text)
