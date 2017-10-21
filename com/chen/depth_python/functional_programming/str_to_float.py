from functools import reduce

def str2float(L):
    dict={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}
    list2=list(map(lambda x:dict[x],L))
    num =len(list2)
    try:
        num=list2.index('.')
    except ValueError:
        return reduce(lambda x,y:x*10+y,list2[:])

    Z=reduce(lambda x,y:x*10+y,list2[:num])
    M=reduce(lambda x,y:0.1*x+y,list2[:num:-1])/10
    S=Z+M
    return S

result = str2float('123.4567')
print(result)
