class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.num = 0

    def desc(self):
        print('name = ' + self.name)
        print('type = ' + self.type)

    def open(self):
        print('the restaurant opened...')

    def print_num(self):
        print("there are", self.num, "people in this restaurant.")

    def add(self):
        self.num = self.num + 1

    def add(self, num=1):
        self.num = self.num + num

def test():
    r1 = Restaurant('zhong', type='la')
    r2 = Restaurant('humberger', type='west')

    print(r1.name)
    print(r1.type)

    r1.desc()
    r1.open()

    r2.desc()
    r2.open()

    r1.add(123)
    r1.print_num()

    r1.add()
    r1.print_num()
