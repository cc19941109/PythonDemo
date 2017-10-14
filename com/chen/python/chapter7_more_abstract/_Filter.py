class Filter:
    def init(self):
        self.blocked = []

    def filter(self, seq):
        return [x for x in seq if x not in self.blocked]


class SpamFilter(Filter):
    def init(self):
        self.blocked = ['Spam']


f = Filter()
f.init()
x = f.filter([1, 2, 3])
print(x)

sf = SpamFilter()
sf.init()
y = sf.filter(['Spam',1,2,3,'ad'])
print(y)

print('------------==')
print(issubclass(SpamFilter,Filter))
print(issubclass(Filter,SpamFilter))

print(isinstance(f,Filter))
print(isinstance(sf,Filter))
print("------------==")
print(SpamFilter.__bases__)
print(Filter.__bases__)

print('\n - - - - ','next str test',' - - - - \n')

print(isinstance('s',str))
print('s'.__class__)
print(type('s'))
print(isinstance('s',str))


