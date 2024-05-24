class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
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

# Output -> true bcx electricCar inherit

print(isinstance(mycar1, Car))
print(isinstance(mycar1, ElectricCar))