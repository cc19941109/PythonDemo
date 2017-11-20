import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_function=None):
    # 这是一个矩阵,里面是随机变量
    # in_size 行数 out_size  列
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))

    # 列表 均为0.1
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)

    # inputs * weights
    Wx_plus_b = tf.matmul(inputs, Weights) + biases


    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# 300行 -1到1
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
# 噪点
noise = np.random.normal(0, 0.05, x_data.shape)

y_data = np.square(x_data) - 0.5 + noise

# 输入层 1个,隐藏层10个,输出层1个 神经元
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
predition = add_layer(l1, 10, 1)  # 与期望的值的差距
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition),
                                    reduction_indices=[1]))
# 常用的优化器,学习效率,最小化差距
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()

# writer = tf.train.SummarySaverHook("logs",sess.graph)

sess.run(init)

# 可视化
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)

plt.ion()
plt.show()

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))

        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass

        # 将predition_value 放到图中,r- 红色的线,宽度为5
        predition_value = sess.run(predition, feed_dict={xs: x_data})
        lines = ax.plot(x_data, predition_value, 'r-', lw=5)
        plt.pause(0.4)

sess.close()
