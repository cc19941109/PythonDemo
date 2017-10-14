class Secretive:

    def __inaccssible(self):
        print('i am __inaccssible')

    def accessible(self):
        print('i am accessible')



foo = Secretive()

foo.accessible()
# foo.__accessible()
foo._Secretive__inaccssible()
