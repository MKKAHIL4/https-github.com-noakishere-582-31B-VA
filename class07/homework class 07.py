from abc import ABC, abstractmethod

#1. ABSTRACT CLASS: VEHICLE

print("====#1. ABSTRACT CLASS: VEHICLE====")

class Vehicle(ABC):
    
    @abstractmethod
    def move(self):
        pass
class car(Vehicle):
    def __init__(self, km):
        self.km = km 
    
    def move(self):
        print("The car drove", self.km, "km on the road.")

class Bicycle(Vehicle):
    def __init__(self, km):
        self.km = km 
    
    def move(self):
        print("The BICYCLE drove", self.km, "km in the park.")

car1 = car(180)
bike1 = Bicycle(12)

car1.move()
bike1.move()

