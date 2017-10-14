class Person(object):
    name = 'test name'
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print('hello',self.name)


foo = Person()
# foo.greet()
# foo.setName('cc')
# foo.greet()
# print(foo)
# print(Person)
# print('-------')
foo.name = 'dd'
Person.greet(foo)
