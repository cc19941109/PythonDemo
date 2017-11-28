
def test():
    for i in range(6):
        yield i
        print('test i')
    print('test...')

x = test()
# print(x)


for item in x :
    # print(item)
    print(' - --- -- - - -- - -- - --')