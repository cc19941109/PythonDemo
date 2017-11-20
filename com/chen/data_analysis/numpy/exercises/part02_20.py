import numpy as np


def q11():
    '''11. Create a 3x3 identity matrix (★☆☆)'''
    x = np.eye(3)
    print(x)
    pass


def q12():
    '''12. Create a 3x3x3 array with random values (★☆☆)'''
    x = np.random.random(27).reshape(3, 3, 3)
    print(x)
    y = np.random.random([3, 3, 3])
    print(y)
    pass


def q13():
    '''13. Create a 10x10 array with random values
    and find the minimum and maximum values (★☆☆)'''
    x = np.random.random((10, 10))
    num_max = np.max(x)
    num_min = np.min(x)
    print(num_max)
    print(num_min)

    print(x.max())
    print(x.min())
    pass


def q14():
    '''14. Create a random vector of size 30 and find the mean value (★☆☆)'''
    x = np.random.random(30)
    y = x.mean()
    print(y)

    pass


def q15(high):
    '''15. Create a 2d array with 1 on the border and 0 inside (★☆☆)'''
    x = np.zeros((high, high))
    x[0, :] = 1
    x[:, 0] = 1
    x[high - 1, :] = 1
    x[:, high - 1] = 1
    print(x)

    pass


def q15_2():
    Z = np.ones((10, 10))
    Z[1:-1, 1:-1] = 0
    print(Z)


def q16():
    '''16. How to add a border (filled with 0's) around an existing array? (★☆☆)'''
    Z = np.ones((5, 5))
    Z = np.pad(Z, pad_width=2, mode='constant', constant_values=0)
    print(Z)
    pass


def padwithtens(vector, pad_width, iaxis, kwargs):
    vector[:pad_width[0]] = 0
    vector[-pad_width[1]:] = 0
    return vector


def q16_test():
    a = np.arange(12).reshape(3, 4)

    y = np.lib.pad(a, 1, padwithtens)
    print(y)
    pass


def q17():
    '''17. What is the result of the following expression? (★☆☆)'''

    print(0 * np.nan)
    print(np.nan == np.nan)
    print(np.inf > np.nan)
    print(np.nan - np.nan)
    a = 0.3 * 1
    print(0.3 == a)

    pass


def q18():
    '''18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)'''
    Z = np.diag(np.arange(1, 5), k=-1)
    print(Z)
    pass


def q19():
    '''19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)'''
    Z = np.zeros((8, 8), dtype=int)
    Z[1::2, ::2] = 1
    Z[::2, 1::2] = 1
    print(Z)

    pass


def q20():
    '''20. Consider a (6,7,8) shape array,
     what is the index (x,y,z) of the 100th element?'''
    a = np.arange(6 * 7 * 8)
    print(np.unravel_index(100, (6, 7, 8)))

    pass

def unravel_index_test():
    x = np.unravel_index([1,1,2], (6,7,8))
    print(x)
    y = np.unravel_index([22, 41, 37], (7, 6))
    print(y)

    z1 = np.unravel_index(22,(7,6))
    print(z1)

    z2 = np.unravel_index(41,(7,6))
    print(z2)

    z3 = np.unravel_index(37,(7,6))
    print(z3)


unravel_index_test()


# 如果indices参数是一个向量的，那么通过该向量中值求出对应的下标。
# 下标的个数就是矩阵的维数，每一维下标组成一个向量，所以返回的向量的个数=矩阵维数。
# 如7*6的矩阵，第22个元素是 3*6+4，所以对应的下标是(3,4)，那么返回的值是 array([3]),array([4])