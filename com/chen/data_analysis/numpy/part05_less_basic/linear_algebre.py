import numpy as np

a = np.array([[1, 2],
              [3, 4]])

# 转置
print(a.transpose())

# 计算矩阵的逆
x = np.linalg.inv(a)
print(x)

# 单位矩阵
# Return a 2-D array with ones on the diagonal and zeros elsewhere.
u = np.eye(4)
print(u)

# 矩阵 点乘
j = np.array([[0.0, -1.0], [1.0, 0.0]])
j1 = np.dot(j, j)
print(j1)

# 返回对角线元素之和
trace1 = np.trace(u)
print(trace1)


# 解线性矩阵方程或线性标量方程组
y = np.array([[5.], [7.]])
result_y = np.linalg.solve(a, y)

print(result_y)

# 正方形数组的特征值和右特征向量的计算
result_eig = np.linalg.eig(j)
print(result_eig)



