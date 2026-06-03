#exceptions

#1. Bank Account

# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance
        
#     def deposit(self, amount):
#         if amount < 0:
#             raise ValueError("Deposit cannot be negative!.")
        
#         self.__balance += amount
    
#     def withdraw(self, amount)
#         if amount < 0:
#             raise ValueError("Withdraw cannot be negative")
        
#         if amount > self.__balance:
#             raise ValueError("Insufficient funds")
#         self.__balance -= amount
    
#     def get_balance(self):
#         return self.__balance
    
# try:
#     account = BankAccount(100)
#     account.deposit(50)
#     account.withdraw(25)
    
#     print("Balance: ", account.get_balance())
# except ValueError as error:
#     print("Bank Account Error:", error)
    
#2. temperature class
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("temperature is below absolute Zero")
        self.__celsius = value
    
try:
    temp = Temperature(-300)

except ValueError as error:
    print("Temperature Error:", error)
    
    
#3 Custom Exceptions and product class
class NegativePriceError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise NegativePriceError("Price cannot be negative")
        
        self.__price = value
        
try:
    product = Product("PC", -500)

except NegativePriceError as error:
    print("Product Error:", error)
    
class DepositError(Exception):
    pass

class NegativeWithdrawalError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class Account:
    def init_(self, owner, balance):
        self.owner = owner
        self.balance - balance

@property
def owner(self):
    return self. owner

@owner.setter
def owner(self, value):
    if not value.strip():
        raise ValueError("Owner's name cannot be empty")
    self. owner - value

@property
def balance(self):
    return self. balance

@balance.setter
def balance(self, value):
    if value < 0:
        raise ValueError("Balance should be more or equal to zero")
    self. balance = value

def deposit(self, amount):
    if amount < 0:
        raise DepositError("The amount to deposit should be a positive number")
    self.balance += amount

def withdraw(self, amount):
    if amount < 0:
        raise NegativeWithdrawalError("The amount withdrawn should be a positive number")
    if amount > self.balance:
        raise InsufficientFundsError("There is not enough money in your account")
    self.balance -= amount