import numpy as np


def fancy_index():
    a = np.arange(12) ** 2
    i = np.array([1, 1, 3, 8, 5])

    print(a[i])

    j = np.arange(1, 12, 2).reshape(2, 3)

    print(a[j])


# fancy_index()

def fancy_index_two():
    a = 2 ** np.arange(12).reshape((3, 4))
    print(a)

    i = np.array([[0, 1],
                  [1, 2]])
    j = np.array([[2, 1],
                  [3, 3]])

    print(a[i])
    print(' -- - - -- - - - ')

    # print(a[i, 2])
    # print(' -- - - -- - - - ')
    # print(a[i, j])
    # print(' -- - - -- - - - ')
    # print(a[:,j])
    # 每一行分别取第2,1,3,3位

    print(' - - -- - -- -')
    x = [i, j]
    print(a[x])


# fancy_index_two()


def list_array():
    i = np.array([[0, 1],
                  [1, 2]])
    j = np.array([[2, 1],
                  [3, 3]])
    x = [i, j]
    print(x)

    s = np.array(x)

    print(s)


# list_array()


def search_time_max():
    time = np.linspace(20, 145, 5)
    print(time)
    data = np.sin(np.arange(20)).reshape(5, 4)
    print(data)
    ind = data.argmax(axis=-2)
    print(ind)


def assign():
    a = np.arange(5)
    a[[1, 2]] = [112, 113]
    print(a)


def add_equal_array():
    a = np.arange(5)
    a[[0, 1, 2]] += 10
    print(a)


def mul_equal_array():
    a = np.arange(5)
    a[[1, 2]] *= 11
    print(a)


def boolean_array():
    a = np.arange(12).reshape(3, 4)
    b = a % 3 == 0
    print(b)
    print(a[b])
    a[b] = 9999
    print(a)


def boolean_array2():
    a = np.arange(12).reshape(3, 4)
    print(a)

    b1 = np.array([False, True, True])
    b2 = np.array([True, False, True, False])
    x = a[b1]
    print(x)
    print(' -- - - -- - -')
    print(a[b1, :])
    print(' - -- -- - -')
    print(a[:, b2])
    print('-  --- -- - - -- - ')
    print(a[b1, b2])


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

def ix_fuc_test():
    ax, bx, cx = np.ix_(a, b, c)
    print(ax, ax.shape)
    print('  -- -- - --  - -  ')
    print(bx, bx.shape)
    print(' - -- -- - - - - -- ')
    print(cx, cx.shape)
    print('- - - - -- - -')
    result = ax + bx * cx
    print(result)
    print(result[1, 2, 2], a[1] + b[2] * c[2])


def ufunc_reduce(ufct, *vectors):
    vs = np.ix_(*vectors)
    r = ufct.identity
    for v in vs:
        r = ufct(r, v)

    return r

r = ufunc_reduce(np.add,a,b,c)
print(r)
