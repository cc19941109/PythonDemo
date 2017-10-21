# 返回函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

x =lazy_sum(1,2,3,4,5,5)
print(x())
