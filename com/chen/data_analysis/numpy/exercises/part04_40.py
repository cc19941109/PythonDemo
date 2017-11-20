import numpy as np

# Suicide mode on
# defaults = np.seterr(all="ignore")
# Z = np.ones(1) / 0

# Back to sanity
# _ = np.seterr(**defaults)
# print(_)

with np.errstate(divide='ignore'):
    Z = np.ones(1) / 0


def test():
    Z = np.ones(1) / 0

test()
