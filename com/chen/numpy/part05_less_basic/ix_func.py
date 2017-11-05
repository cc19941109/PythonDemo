import numpy as np

def test():
    a = np.arange(10).reshape(2,5)
    ixgrid = np.ix_([0,1],[2,4])

    print(ixgrid)
    print(type(ixgrid))

test()