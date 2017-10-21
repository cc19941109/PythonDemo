isOdd = lambda x: x % 2 == 0

x = filter(isOdd, [1, 2, 3, 4, 5, 6, 7])
x = filter(lambda x:x%2==0, [1, 2, 3, 4, 5, 6, 7])
print(list(x))

print('\n- - - - - - ')


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
