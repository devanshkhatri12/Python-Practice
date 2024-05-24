# static method ->  ek esa method jo class k pass toh available bt obj(instance) se access nhi h

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def fuel_type(self):
        return ("petrol or disel")
    
    @staticmethod
    def general_description():                  # noconnection for access req. ->  like self arg. when we access using class name 
        return "Car are means of transport !"
    
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return ("Electric charge")
    

mycar1 = ElectricCar("Tesla", "model R")

mycar2 = Car("Tata", "model S")

# print(mycar1.general_description())             # cant access using instance bcz static method

print(Car.general_description())