class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_desc(self):
        str1 = str(self.year) + " " + self.make + " " + self.model
        return str1.title()

    def read_odometer(self):
        print("this car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, odometer):
        if odometer > self.odometer:
            self.odometer = odometer
        else:
            print("you can't roll back an odometer")

    def add_odometer(self):
        self.odometer += 1


def test():

    car1 = Car('audi', 'a4', 2017)
    print(car1.get_desc())

    car1.odometer = 1231
    car1.read_odometer()

    car1.update_odometer(1424)
    car1.read_odometer()

    car1.add_odometer()
    car1.read_odometer()

    car1.update_odometer(1242)
