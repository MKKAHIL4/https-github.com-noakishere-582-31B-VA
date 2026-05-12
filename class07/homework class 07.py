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
        print(f"The car drove {self.km} km on the road.")

class Bicycle(Vehicle):
    def __init__(self, km):
        self.km = km 
    
    def move(self):
        print(f"The BICYCLE drove {self.km} km in the park.")

car1 = car(180)
bike1 = Bicycle(12)

car1.move()
bike1.move()

print("\n")
#2. ABSTRACT CLASS: FILE HANDLER
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self):
        pass
    
    #text file handler
    
class TextFileHandler(FileHandler):
    
    def read(self):
        print(f"Reading student notes from notes.txt")
        
    def write(self):
        print(f"Writing homework into notes.txt")

#JsonFileHnadler

class JsonFileHandler(FileHandler):
    def read(self):
        print(f"Reading User settings from settings.josn")
        
    def write(self):
        print(f"Writing Homework into setting.json")
        
print("#2.====== ABSTRACT CLASS : FILE HANDLER ======")
textFile = TextFileHandler()
jsonFile = JsonFileHandler()

textFile.read()
textFile.write()

jsonFile.read()
jsonFile.write()
print("\n")

#3. ABSTRACT CLASS : ACCOUNT
class Account(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass
#Savings account
class SavingsAccount(Account):
    def calculate_fee(self):
        return 4.99

#PremiumAccount
class premiumAccount(Account):
    def calculate_fee(self):
        return 24.99
    
print("======#3. ABSTRACT CLASS : ACCOUNT ======")

savingAcc = SavingsAccount()
premiumAcc = premiumAccount()

print(f"Savings Account Monthly fee: ${savingAcc.calculate_fee()}")
print(f"Premium Account Monthly fee: ${premiumAcc.calculate_fee()}")

print("\n")




