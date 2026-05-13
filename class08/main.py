#encapsulation

class Book:
    def __init__(self, name):
        self.name = name 
    
book1 = Book("test")
book1.name = "something else"

print(book1.name) 
#public -- data can be accessed from anywhere inside or outside the class
#private -- protects the data from bieng accessed directly outside the class
#ex: private name 

#in python, we only use naming conventions and developer responsibility

#python trust the programmer more
#visibility (public, private) is about communication and design not just compiler-enforced rules!

#so far weve seen:
#classes
#inst attributes
#instance method
#class atributes
#static methods
#abstraction and interfaces

#let's bring in encapsulation here:
#poorly encapsulated example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
acc1 = BankAccount("Alice", 500)
acc1.balance = -1000

#how can we make it better
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount)
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def show_balance(self)
        print(f"balance is : {self.__balance}")

bank_account1 = BankAccount("Jane", 500)
#bank_account1.__balance = 1000 # this would throws an error
# the method is handling interaction
bank_account1.deposit(500)# deposit() handle data internallly
bank_account1.show_balance()# show balance() accesses data ionternally and shows us!
bank_account1.withdraw(200)#withdraw handles data internally
bank_account1.show_balance()# show balance() accesses data ionternally and shows us!

#why is thsi better?
#rules are handled through methods
#raw external data mtation/change is prohibited

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def set_celsius(self, value):
        pass
    def show_celsius(self):
        print(f"{self.__celsius} C")
        
temp1 = Temperature(8)
temp1.set_celsius(23)
temp1.show_celsius()



# we need to protect our code from ourselves!

#ecaplsulation means keeping data and the rules using that data together inside the class
#it also means:
#limiting direct access to internal details
#protecting object state from invalid changes
#exposing a cleaner public interface
# we want our class to help control how that data is used 

# we have three naming patterns to signal intended visibility

# public
name = "hi"
class Student:
    def __init__(self,name):
        self.name = name
student1 = Student("John")
student1.name="Ali"
#2.private 
__name = "hi"

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa #prvt attribute
student2 = Student("Alice", 3.8) # this would fail, because the concept of name magling

#3. protected 
_name = "hi"  

#what is name mangling?
#when an attribute starts with__ inside a class python changes its internal name to reduce accidental
#access and accidental overriding

student3 = Student("jane", 3.5)
print(student3.__dict__)
# we see that __gpa has been transformed to _Student__gpa internally.

print(student3.Student__gpa)
#print(student3.__gpa) # this doesnt show anything and throws an error

#the goal of using this private accessor is to 
#avoid accidental direct access

