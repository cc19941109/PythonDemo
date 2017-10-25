import requests

# https://api.github.com/rate_limit 测试访问限制

# 执行 api 调用并存储响应
url= 'https://www.zhihu.com/'
r = requests.get(url)
print('Status code:',r.status_code)


# 将 API 响应存储在一个变量中
response_dict = r.json()
print("total repositories:".title(),response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('repositories returned:'.title(),len(repo_dicts))

