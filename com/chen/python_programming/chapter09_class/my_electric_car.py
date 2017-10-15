# from  _class_electricCar import ElectricCar,Battery
import _class_electricCar

car1 = _class_electricCar.ElectricCar('china','A4',2015)
print(car1.get_desc())
car1.battery.desc_battery()


car2 = _class_electricCar.Car('china','A4',2015)
x = car2.get_desc()
print(x)