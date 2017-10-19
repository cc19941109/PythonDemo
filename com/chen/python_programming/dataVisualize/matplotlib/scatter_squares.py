import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]


# 越靠近0,颜色越深,值越靠近1,指定颜色越浅
plt.scatter(x_values,y_values,s = 10,edgecolors='none',c = y_values,cmap=plt.cm.Blues)
# plt.scatter(x_values,y_values,s = 10,edgecolors='none',c = (0,0,0.99))
# plt.scatter(x_values,y_values,s = 10,edgecolors='none',c = 'red')

plt.axis([0,1100,0,1100000])
plt.savefig('square_plot.png',bbox_inches = 'tight')
plt.show()


