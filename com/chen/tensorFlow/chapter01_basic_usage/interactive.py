# 进入一个交互式 TensorFlow 会话.
import tensorflow as tf
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

# 使用初始化器 initializer op 的 run() 方法初始化 'x'
x.initializer.run()

# 增加一个加法 sub op, 从 'x' 加 'a'. 运行加法 op, 输出结果
sub = tf.add(x, a)
print(sub.eval())
# ==> [4. 5.]

