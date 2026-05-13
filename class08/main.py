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
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
acc1 = BankAccount("Alice", 500)
acc1.balance = -1000

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

