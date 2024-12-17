class Car:
    def __init__(self):
        #initialize the Car with default attributes
        self.make="Toyota"
        self.model="Corolla"
        self.year=2020
#create an instance using the default constructor 
car=Car()
print(car.make)
print(car.model)
print(car.year)