class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1              # every time object is created the constructor will call

    def fuel_type(self):
        return ("petrol or disel")
    
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return ("Electric charge")
    

mycar1 = ElectricCar("Tesla", "model R")

mycar2 = Car("Tata", "model S")



print(mycar1.fuel_type())
print(mycar2.fuel_type())

print(Car.total_car)

mycar3 = Car("tata", "tiago")

print(Car.total_car)