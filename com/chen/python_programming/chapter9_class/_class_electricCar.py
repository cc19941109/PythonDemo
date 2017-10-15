from _class_car import Car

class Battery():
    """电动汽车的电瓶"""

    def __init__(self,battery_size = 70):
        """初始化电瓶的容量"""
        self.battery_size = battery_size

    def desc_battery(self):
        print("this car has a ",self.battery_size,"-kWh battery.")


class ElectricCar(Car):
    """电动汽车"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery= Battery()

    def read_battrey_size(self):
        print('the battery size is',self.battery.battery_size)

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


def test():

    ecar1  = ElectricCar('tesla','model s',2017)
    print(ecar1.get_desc())
    ecar1.read_battrey_size()

    ecar1.battery.desc_battery()





