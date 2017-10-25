import requests

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行 api 调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# 将 API 响应存储在一个变量中
response_dict = r.json()
print("total repositories:".title(), response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('repositories returned:'.title(), len(repo_dicts))
print(repo_dicts)

names, stars = [], []
urls = []

plot_dicts = []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {'value': repo_dict['stargazers_count'],
                 # 'label': repo_dict['description'],
                 'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
# 隐藏图表中的水平线
my_config.show_legend = False

my_config.title_font_size = 24
my_config.label_font_size = 10
my_config.major_label_font_size = 18

# 将较长的项目名缩短为15个字符
my_config.truncate_label = 15

my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "most-starred python projects in github".title()
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('Python_repos.svg')
