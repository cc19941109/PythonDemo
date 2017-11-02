import numpy as np

a = np.floor(10 * np.random.random((2, 2)))
b = np.floor(10 * np.random.random((2, 2)))

x = np.vstack((a, b))

print(x.shape)
print(x)

y = np.hstack((a, b))
print(y.shape)
print(y)
help(np.hstack)

# np.concatenate`` or ``np.stack

print(a)
print(b)

# stack : Join a sequence of arrays along a new axis.
#     vstack : Stack arrays in sequence vertically (row wise).
#     dstack : Stack arrays in sequence depth wise (along third axis).
#     concatenate : Join a sequence of arrays along an existing axis.
#     hsplit : Split array along second axis.
#     block : Assemble arrays from blocks.