import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 23, 4, 46, 7, np.nan])
s.name = "num"
print(s)

#  Return a fixed frequency DatetimeIndex 返回固定频率的时间 index
dates = pd.date_range('20130101', periods=6)
print("dates", dates)

# 从正态分布返回结果 通过 ndarray 创建,with a datetime index and labeled columns:
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 通过字典创建
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)

print('\n- - -- - -')

# 查看dataFrame 内部的数据类型
print(df.dtypes)
print('- - -- - -\n')

# See the top & bottom rows of the frame
#  The default number of elements to display is five
print(df.head(6))
print(df.tail(3))
print('\n- - ----- --- ----- ---- -- ----- ---- ')
print('- - ----- --- ----- ---- -- ----- ---- ')
print()

print(df.index)
print(df.columns)
a = df.values

print(a)
print(type(a))


# Describe shows a quick statistic summary of your data
print(df.describe())

print('\n- - ----- --- ----- ---- -- ----- ---- ')
print('- - ----- --- ----- ---- -- ----- ---- ')
print()

# 转置并不改变自身, 但是返回
print(df.T)

# index 排序,原 dataFrame 不变,0 给index名字排序, 1给 column名字排序
df_sort = df.sort_index(axis=1, ascending=True)
print(df_sort)

print('\n- - ----- --- ----- ---- -- ----- ---- ')
print('- - ----- --- ----- ---- -- ----- ---- ')
print()

df_sort2 = df.sort_values(by='B',ascending=False)
print(df_sort2)