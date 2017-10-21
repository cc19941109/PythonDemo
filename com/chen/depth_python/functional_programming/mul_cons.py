from functools import reduce

mul = lambda x,y:x*y

def prod(l):
    return  reduce(mul,l)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))