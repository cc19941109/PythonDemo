import _class_restaurant

class IceCreamStand(_class_restaurant.Restaurant):
    def __init__(self, name, type):
        super(IceCreamStand, self).__init__(name,type)
        self.flavors = []

    def add(self, name):
        self.flavors.append(name)

    def print_flavors(self):
        print(self.flavors)


iceCream = IceCreamStand('iceCreamStand','iceCream')
iceCream.add('cc')
iceCream.print_flavors()
iceCream.print_num()

