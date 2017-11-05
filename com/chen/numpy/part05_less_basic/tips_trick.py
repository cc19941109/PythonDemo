# “Automatic” Reshaping,Vector Stacking,Histograms
import numpy as np
import matplotlib.pyplot as plt


def test():
    a = np.arange(30)

    # -1 means "whatever is needed"
    a.shape = 2, -1, 3
    print(a.shape)
    print(a)

    print('- - -- -  - --')
    x = np.arange(0, 10, 2)  # x=([0,2,4,6,8])
    y = np.arange(5)  # y=([0,1,2,3,4])
    m = np.vstack([x, y])  # m=([[0,2,4,6,8],
    #     [0,1,2,3,4]])
    xy = np.hstack([x, y])  # xy =([0,2,4,6,8,0,1,2,3,4])

    print(m)
    print(xy)


def test2():
    mu, sigma = 2, 0.5
    v = np.random.normal(mu, sigma, 10000)
    plt.hist(v, bins=50, normed=1)
    plt.show()

test2()


