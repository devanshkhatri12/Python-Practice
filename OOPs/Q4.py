class Car:
    def __init__(self, brand, model):
        self.__brand = brand            # make brand private using (__)
        self.model = model

    def get_brand(self):                # access only in class
        return self.__brand + "!"
    

Mycar = Car("Tesla", "model r")

# print(Mycar.__brand)
print(Mycar.get_brand())

        