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
    
    def __init__(self, owner):
        self.owner = owner
        
    def showType(self):
        return f"{self.owner} has a regular account"

        
class SavingsAccount(Account):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate
    
    def showType(self):
        return f"{self.owner} has a saving account with interest rate of {self.interest_rate}"
class PremiumAccount(Account):
    def __init__(self, owner, reward_level):
        super().__init__(owner)
        self.rewrad_level = reward_level
    
    def showType(self):
        return f"{self.owner} has a premium account with rewrad levelof {self.rewrad_level}"

accounts = [Account("Kamyar"), SavingsAccount("Moe", 7.5), PremiumAccount("Evgeniya", "Gold")]


for account in accounts:
    print(account.showType())