class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"Recently bought {self.brand} car {self.model} model"


myCar = Car("TATA", "Range Rover")
print(myCar.brand)
print(myCar.model)
print(myCar.fullname())
        