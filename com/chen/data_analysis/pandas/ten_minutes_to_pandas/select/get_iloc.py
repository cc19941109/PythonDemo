import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  Return a fixed frequency DatetimeIndex 返回固定频率的时间 index
dates = pd.date_range('20130101', periods=10)
# print("dates", dates)

# 从正态分布返回结果 通过 ndarray 创建,with a datetime index and labeled columns:
df = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list('ABCD'))
print(df)

print('\n- - -- - -')


print(df.iloc[0])
x1 = df.iloc[3:5,0:2]
print(x1)

x2 = df.iloc[[1, 2, 4], [0, 2]]
print(x2)


print(df.iloc[1,1])