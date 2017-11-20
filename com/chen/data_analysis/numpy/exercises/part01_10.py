import numpy as np


def q02():
    print(np.__version__)
    np.show_config()


def q03():
    ''' Create a null vector of size 10 创建一个size 为10 的空向量'''
    x = np.zeros(10)
    print(x)

    pass


def q04():
    '''How to find the memory size of any array'''
    a = np.arange(234, dtype=np.float128)
    print(a.size)
    print(a.itemsize)
    print(a.dtype)

    pass


def q05():
    np.info(np.add)

    pass


def q06():
    '''6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)'''
    x = np.zeros(10)
    x[4] = 1
    print(x)

    pass


def q07():
    x = np.arange(10, 50)
    print(x)
    pass


def q08():
    '''8. Reverse a vector (first element becomes last) (★☆☆)'''
    x = np.arange(0, 100, 3)
    y = x[::-1]
    print(y)
    pass


def q09():
    '''9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)'''
    x = np.arange(0,9,1).reshape(3,3)
    print(x)

    pass

def q10():
    '''10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)'''
    x = np.array([1,2,0,0,4,0])
    y = np.where(x!=0)
    print(y)
    pass

q10()

def q10_2():
    nz = np.nonzero([1, 2, 0, 0, 4, 0])
    print(nz)

q10_2()