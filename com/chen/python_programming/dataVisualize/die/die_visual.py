import pygal

from die import Die

# 根据数据生成柱状图
# 产生 svg 文件
# TODO: 写成函数

die = Die()
die2 = Die()

results = []
for x in range(1000):
    result = die.roll()+die2.roll()
    results.append(result)

print(list(results))
frequencies = []
max_result = die.num_sides+die2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 作图
# 这个图片打开要联网?

hist = pygal.Bar()

hist.title = 'Results of rolling two D6 1000 times'
hist.x_labels = ['2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12']
hist.x_title = 'result'.title()
hist.y_title = 'frequency of result'.title()

hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual.svg')

