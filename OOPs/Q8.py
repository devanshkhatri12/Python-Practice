class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model              # make it private

    def fuel_type(self):
        return ("petrol or disel")
    
    @property                             # make it read only 
    def model(self):
        return self.__model
    

    
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return ("Electric charge")
    

mycar2 = Car("Tata", "model S")
# mycar2.model = "A8"                 # we make it non changable


print(mycar2.model)
print(mycar2.fuel_type())

print(mycar2.model())
print(mycar2.model)

mycar1 = ElectricCar("tesla", "model Q")

print(mycar1.brand)
print(mycar1.model)

