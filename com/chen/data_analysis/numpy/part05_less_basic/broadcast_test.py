import numpy as np


def test1():
    '''测试长度不同时相加会产生怎么样的结果'''
    a = np.array([[0.0, 0.0, 0.0],
                  [10.0, 10.0, 10.0],
                  [20.0, 20.0, 20.0],
                  [30.0, 30.0, 30.0]])
    b = np.array([1., 2., 3.])
    print(a.shape)
    print(b.shape)
    print(a * b)


def test2():
    '''测试长度不同时相加会产生怎么样的结果'''
    a = np.array([[0.0, 0.0, 0.0],
                  [10.0, 10.0, 10.0],
                  [20.0, 20.0, 20.0],
                  [30.0, 30.0, 30.0]])
    b = np.array([1., 2., 3., 4.])
    print(a.shape)
    print(b.shape)
    print(a * b)
    # operands could not be broadcast together with
    # shapes (4,3) (4,)


# test1()
# print(' -- - - -- - -- - - ')
# test2()



def test3():
    a = np.array([0., 10., 20., 30.])
    b = np.array([1., 2., 3.])
    print(a.shape)
    print(a[:, np.newaxis].shape)
    print(a[:, np.newaxis] + b)


# test3()


def test4_minus():
    a = np.array([0., 10., 20., 30.])
    b = np.array([1., 2., 3.])
    print(a[:,np.newaxis]-b)

# test4_minus()
# 减法和加法的效果一致


def test5():
    observation  = np.array([1,2,3,4])
    codes = np.array([[2,3],
                      [3,4],
                      [5,6],
                      [7,8]])
    diff = codes -observation[:,np.newaxis]

    print(diff)

# test5()


def test6():
    observation  = np.array([7,5])
    codes = np.array([[2,3],
                      [3,4],
                      [5,6],
                      [7,8]])
    diff = codes-observation

    dist_2 =np.sum(diff**2,axis=-1)
    print(dist_2)
    dist = np.sqrt(dist_2)

    print(dist)
    print(np.min(dist))
    print(np.argmin(dist))

test6()



