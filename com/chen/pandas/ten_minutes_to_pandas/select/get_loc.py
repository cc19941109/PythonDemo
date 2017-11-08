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

print(df['A'])

print(df[:7:2])

x = df['20130102':'20130110':2]
print(x)


print('\n- -- - -- - - - -- \n')

x1 = df.loc[dates[0]]

print(x1)

x2 = df.loc['20130102':'20130104',['A','B']]
print(x2)

x3 = df.loc['20130101','A']
print(x3)