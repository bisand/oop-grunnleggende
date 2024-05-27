class Car:
    instanceCount: int = 0
    cars = []

    def __init__(self, brand: str = "Toyota", model: str = "Corolla", year: int = 2000, speed: int = 100) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        Car.instanceCount += 1
        Car.cars.append(self)

    def __str__(self) -> str:
        return f"This is a {self.brand} {self.model}, made in {self.year}, and can run in {self.speed} km/h"

    def __repr__(self) -> str:
        return f"Car('{self.brand}','{self.model}','{self.year}','{self.speed}')"
    
    def __del__(self):
        print(f"Destroying the {self.brand}")
        Car.instanceCount += 1
        Car.cars.remove(self)

    @classmethod
    def printAvailableCars(cls):
        for car in cls.cars:
            print(car)

    def increaseSpeed(self, speed: int):
        self.speed += speed

    def printSpeed(self):
        print(f"Max speed is: {self.speed} km/h")

    def printInstaceCount(self):
        print(f"Instances: {Car.instanceCount}")

volvo = Car("Volvo", "XC60", 1990, 98)
tesla = Car("Tesla", "Model 3", 2023, 200)
lada = Car("Lada", "2000")
ford = Car()
Car.printAvailableCars()


tesla.printSpeed()
tesla.increaseSpeed(10)
tesla.printSpeed()

del ford

print(volvo)
print(tesla)

print(volvo.__repr__())
