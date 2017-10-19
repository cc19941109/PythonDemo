import matplotlib.pyplot as plt

from random_walk import RandomWalk

# while True:

rw = RandomWalk(5000)
rw.fill_walk()
point_numbers = list(range(rw.num_points))

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, s=4)
# plt.scatter(rw.x_values, rw.y_values, c=point_numbers ,cmap=plt.cm.Blues,s=10)

# 画出 起点和终点
plt.scatter(0, 0, c='green', s=30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', s=30)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# plt.figure(dpi=128,figsize=(5,4))


plt.show()


# keep_running = input("make another walk?(y/n)\n:")
# if keep_running =='n':
#     break
