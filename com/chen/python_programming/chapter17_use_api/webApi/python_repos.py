import requests

# https://api.github.com/rate_limit 测试访问限制

# 执行 api 调用并存储响应
url= 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:',r.status_code)


# 将 API 响应存储在一个变量中
response_dict = r.json()
print("total repositories:".title(),response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('repositories returned:'.title(),len(repo_dicts))


# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

print('\n - - - - - - - - - - - ')


for repo_dict in repo_dicts:
    print('Name:',repo_dict['name'])
    print('Owner',repo_dict['owner'])
    print('Stars:',repo_dict['stargazers_count'])
    print('repository:'.title(),repo_dict['html_url'])
    print('created:'.title(),repo_dict['created_at'])
    print('updated_at:'.title(),repo_dict['updated_at'])
    print('description:'.title(),repo_dict['description'])
    print('\n - - - - - - - - - - - ')

