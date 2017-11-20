import numpy as np


def q21():
    '''21. Create a checkerboard 8x8 matrix
    using the tile function (★☆☆)'''
    x = np.tile(np.array([[0, 1], [1, 0]]), (4, 4)).reshape(8, 8)
    print(x)

    pass


def q22():
    '''22. Normalize a 5x5 random matrix (★☆☆)'''
    Z = np.random.random((5, 5))
    Zmax, Zmin = Z.max(), Z.min()
    Z = (Z - Zmin) / (Zmax - Zmin)
    print(Z)

    # 这是规范矩阵???

    pass


def q23():
    '''23. Create a custom dtype that describes a color
     as four unsigned bytes (RGBA) (★☆☆)'''
    color = np.dtype([("r", np.ubyte, 1),
                      ("g", np.ubyte, 1),
                      ("b", np.ubyte, 1),
                      ("a", np.ubyte, 1)])
    print(color)
    print(type(color))

    # ???
    pass


def q24():
    '''24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)'''
    a = np.arange(15).reshape(5, 3)
    b = np.arange(6).reshape(3, 2)

    x = np.dot(a, b)
    print(x)
    print(' -- - - - -- ')

    y = a @ b
    print(y)
    pass


def q25():
    '''25. Given a 1D array, negate all elements
     which are between 3 and 8, in place. (★☆☆)'''

    Z = np.arange(11)
    Z[(3 < Z) & (Z <= 8)] *= -1
    print(Z)




def q26():
    '''26. What is the output of the following script? (★☆☆)'''
    print(sum(range(5), -1))
    print(np.sum(range(5), 0))

    pass


def q27():
    '''27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)'''
    Z = np.arange(1,5)
    print(Z)
    # print(Z ** Z)

    # 2 左移动1位,2位,3位,4位
    print(2 << Z )
    # 1,2,3,4 右移动2位
    print(Z >> 2)

    print(2 << Z >> 2)

    print(Z < - Z)

    print(1j * Z)

    print(Z / 1 / 1)
    # Z < Z > Z

    pass


def q28():
    '''28. What are the result of the following expressions?'''
    # x1 = np.array(0) / np.array(0)
    # x2 = np.array(0) // np.array(0)
    x3 = np.array([np.nan]).astype(int).astype(float)

    # print(x1)
    # print(x2)
    print(x3)
    pass


def astype_test():
    x = np.array([1.,2.5,-1.5,3.5,-2.5,-0.5,3.8,2.9])
    print(x)
    y = x.astype(int)
    print(y)
    print(x)


def q29():
    '''29. How to round away from zero a float array ? (★☆☆)'''
    Z = np.random.uniform(-10, +10, 10)
    print(Z)
    print(np.copysign(np.ceil(np.abs(Z)), Z))
    pass


def ceil_test():
    a =np.random.uniform(-10,10,10)
    print(a)
    print( '\n -- ceil-- -')
    print(np.ceil(a))
    print( '\n -- floor-- -')
    print(np.floor(a))
    print( '\n -- round-- -')
    print(np.round(a))


def round_test():
    a = np.array([3.5,2.5,1.5,0.5,-1.5,-2.5,-0.5])
    print(np.round(a))


def q30():
    '''30. How to find common values between two arrays? (★☆☆)'''
    a = np.arange(1,8)
    b = np.arange(5,10)

    x =np.intersect1d(a,b)
    print(x)

def copysign_test():
    a = np.random.uniform(-1,1,10)
    b = np.arange(10)

    x = np.copysign(b,a)

    print(x)

copysign_test()
