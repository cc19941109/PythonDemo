class Test(object):
    a = 'one'
    b = 'two'
    huh = locals()
    c = 'three'
    huh['d'] = 'four'
    print(huh)


class Test1(object):
    a = 'one'
    b = 'two'
    def frobber(self):
        print (self.c)
t = Test1()
huh = vars(t)
huh['c'] = 'three'
t.frobber()

