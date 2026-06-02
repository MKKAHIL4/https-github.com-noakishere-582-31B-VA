class Animal:
    def speak(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def speak(self):
        print("wooof")

class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

print("Animal Sounds: ")
for animal in animals:
    animal.speak() 
    

#2
class Vehicle:
    def __init__(self, brand):
        self.brand = brand 
    
    def describe(self):
        print(f"Brand: {self.brand}")
        
class Car(Vehicle):
    def describe(self):
        print(f"{self.brand} Car")
        
    def drive(self):
        print("The Car is driving.")
        
class Bike(Vehicle):
    def describe(self):
        print(f"{self.brand} Bike")
        
    def pedal(self):
        print("The Bike is bieng paddled.")
vehicles = [Car("Lambourghini"), Bike("BMX")] 

print("\n Vehicle Information:") 
for vehicle in vehicles:
    vehicle.describe()
    
#3
class Account:
    def showType(self):
        print("general Account")
        
class SavingsAccount(Account):
    def showType(self):
        print("Savings Account -Earns five percent Interest")
        
class PremiumAccount(Account):
    def showType(self):
        print("Premium Account - Gets points when traveling")
        
        #return super().showType()
accounts = [SavingsAccount(), PremiumAccount()]

print("\nAccount Types:")
for account in accounts:
    account.showType()