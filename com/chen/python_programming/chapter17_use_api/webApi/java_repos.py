import requests

import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS

# 执行 api 调用并存储响应
url= 'https://api.github.com/search/repositories?q=language:java&sort=stars'
r = requests.get(url)
print('Status code:',r.status_code)


# 将 API 响应存储在一个变量中
response_dict = r.json()
print("total repositories:".title(),response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('repositories returned:'.title(),len(repo_dicts))


names,stars=[],[]
urls =[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    urls.append(repo_dict['html_url'])


# 可视化
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style = my_style,x_label_rotation=45,show_legend=False)
chart.title="most-starred python projects in github".title()
chart.x_labels=names

chart.add('',stars)
chart.render_to_file('java_repos.svg')

