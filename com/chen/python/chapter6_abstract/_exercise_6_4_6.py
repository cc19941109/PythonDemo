def story(**kwds):
    print('hello',kwds['name'], 'i am a',kwds['job'])

def power(x,y,*other):
    if other:
        print(other)
    return pow(x,y)

def interal(start,stop= None ,step = 1):
    'test interal ...'
    print(stop)
    if stop is None :
        start,stop=0,start
    result = []
    i = start
    print('i',i)
    print('stop',stop)
    while i<stop:
        result.append(i)
        i+=step
    return result



story(name = 'cc',job='engineer')
y = power(2,4,3,4,5,6)
print(y)

print('-----')

x = interal(10)
print(x)

print('=========')
s =(5,)*2
print(power(*s))

print('====-----===-----=====')

scope = vars()

x = 1
print(scope)
print(scope['__file__'])
