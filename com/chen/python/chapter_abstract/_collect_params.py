
def mprint(name,*params):
    print('i am',name)
    print(type(params)," " ,params)
    for s in params:
        print(s)


mprint('s',1,4,'sad',312,'eqw')
x=  [1,24,'1231',123,'asda',21,'a23d']

mprint(x)
mprint('test')

def mt(**param):
    print(type(param))
    print(param)


mt(x= 1)

def p4(x,y,z = 3,*a,**b):
    print(x,y,z)
    print(a)
    print(b)


p4(1,2,3,4,5,123,13,76,6,cc=1,ss='s')
p4(1,2,1,(1,3),1,faoo = 2)