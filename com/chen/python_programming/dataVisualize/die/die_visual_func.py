from die import Die

import pygal  # 创建一个 D6 和一个 D10

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# 将掷骰子的结果保存在列表中
results = []
for x in range(5000):
    result = die_1.roll() + die_2.roll()+die_3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides+die_3.num_sides

for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Results of rolling D6 and D6 and D6 50000 times'
hist.x_labels = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16','17','18']
hist.x_title = 'result'.title()
hist.y_title = 'frequency of result'.title()

hist.add('D6+D6+D6', frequencies)
hist.render_to_file('die_visual3.svg')
