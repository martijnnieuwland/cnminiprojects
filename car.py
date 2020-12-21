
class Car:
    """Ride on four wheels"""
    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = year
        self.speed = speed

    def __repr__(self):
        return f"""Class: {__class__.__name__}, model, year, speed=0"""

    def __str__(self):
        return f"""This is an object of the class Car. It's a {self.model} from {self.year} going {self.speed} km/h!"""

    def accelerate(self):
        """This method accelerates the car with 5km/h"""
        self.speed += 5
        return self.speed

    def brake(self):
        """This method decelerates the car with 5km/h"""
        if 0 <= self.speed <= 4:
            self.speed = 0
        else:
            self.speed -= 5
        return self.speed

    def honk_horn(self):
        """This method goes beep"""
        print(f"{self.model} goes 'beep beep'")


my_car = Car("XC90", 2012, 1)

print(repr(my_car))
print(my_car)
print(my_car.speed)
my_car.accelerate()
print(my_car.speed)
my_car.brake()
print(my_car.speed)
my_car.brake()
print(my_car.speed)
my_car.honk_horn()
