def hello(name):
    'hello doc'
    print('hello',name,'!')

hello('cc')

def fib(nums):
    'test fib doc 文档化函数 只能用在函数起始的第一行'
    result = [0,1]
    for i in range(nums-2):
        result.append(result[-1]+result[-2])

    print(result)

fib(10)
fib(19)
print(fib.__doc__)

help(hello)