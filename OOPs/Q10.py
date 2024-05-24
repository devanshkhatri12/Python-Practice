class Battery:
    def Battery_info(self):
        return "Battery"

class Engine:
    def Engine_info(self):
        return "Engine"


class ElectricCar(Battery, Engine):
    pass

mycar = ElectricCar()
print(mycar.Battery_info())
print(mycar.Engine_info())