import numpy as np

a = np.floor(10 * np.random.random((2, 2)))
b = np.floor(10 * np.random.random((2, 2)))


x = np.column_stack((a,b))
print(x)

y = np.hstack((a,b))
print(y)

# help(np.column_stack)
print("\n- - - --  - -- - -- \n")

q = np.array([1,2])
p = np.array([3,4])

qp = np.column_stack((q,p))
print(qp)

print(np.hstack((q,p)))

print("\n- - - --  - -- - -- \n")

print(q[:,np.newaxis])
print("\n- - - --  - -- - -- \n")

test = np.column_stack((q[:,np.newaxis],p[:,np.newaxis]))
print(test)

print("\nlast: - -- - - \n")
print(np.hstack((q[:,np.newaxis],p[:,np.newaxis])))

