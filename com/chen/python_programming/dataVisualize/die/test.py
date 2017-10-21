import pygal

frequencies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

hist = pygal.Bar()

hist.title = 'Results of rolling D6 and D10 50000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'result'.title()
hist.y_title = 'frequency of result'.title()

hist.add('D6+D10', frequencies)
hist.render_to_file('die_visual4.svg')
