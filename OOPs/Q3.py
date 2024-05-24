class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

    def order(self):
        return f"Bought {self.brand} of {self.model} with battery capacity of {self.batterysize} "


Tesla = ElectricCar("Tesla", "model R", "90kwh")

print(Tesla.batterysize)
print(Tesla.order())