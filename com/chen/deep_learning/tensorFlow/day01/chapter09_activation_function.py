# linear func 线性函数 y = Wx
# 但是现实中的问题大部分都不是线性问题
# 我们需要激励函数 y = AF(Wx)

# 特别多层隐藏神经网络, 小心梯度爆炸/消失

# 少量层,有多种选择

# 卷积  relu
# 循环神经网络 relu/tanh

# tf.nn.relu()  小于0 则等于0,大于0 线性y = x

# softplus 在分类问题中使用

# dropout 减少 overfitting 过度拟合的影响

# sigmoid S状 在分类问题中使用

# tanh 正切

# 都是为了解决非线性的问题