#class attributes vs instance attributes

class Student:
    def __init__(self, name, program):
        self.name = name 
        self.program = program
        
student1 = Student("Alice", "web development")
student2 = Student("karim", "Computer Science")
print(student1.name)
print(student2.name)
    
    #what if all students were from the same school?
    #the idea is :
    # some data belong to :
    
    
    
class Student:
    school_name = "Vanier College"
    def __init__(self, name, program):
    #these are instance attributes / perobject state
        self.name = name 
        self.program = program
student1 = Student("Alice", "web development")
student2 = Student("karim", "Computer Science")
print(student1.name)
print(student2.name)

print(student1.school_name)
print(student2.school_name)

#VISUAL COMPARISON
#INSTANCE ATTRIBUTES:
#CREATED WITH SELF
#USUALLY SET IN __INIT
#DIFFERENT PER OBJECT
#CLASS ATTRIBUTES:
#DEFINED IN CLASS BODY
#SHARED ACROOS ALL INSTANCES
#USED FOR COMMON DATA OR CLASS LEVEL CONFIGURATION
class Product:
    category = "Electronics" # shared

    def __init__(self, name, price):
        self.name = name # per object
        self.price = price # per object

product1 = Product("Keyboard", 10)
product2 = Product("Mouse", 25)

product1.price = 8

print(product1.price)
print(product2.price)
print(product1.category)
print(product2.category)

#shadowing a class attribute
class Employee:
    bonus = 0.5
    
    def __init__(self, name):
        self.name = name #this is an instance attribute
        
employee1 = Employee("John")
employee2 = Employee("Jane")
        
Employee.bonus = 1 #change class attribute globally
        
print(f"employee1 bonus : {employee1.bonus}")
print(f"employee2 bonus : {employee2.bonus}")

Employee.bonus = 2 #change class attribute globally
employee3 = Employee("test")     
print(f"employee1 bonus : {employee1.bonus}")
print(f"employee2 bonus : {employee2.bonus}")
print(f"employee3 bonus : {employee3.bonus}")
#the process above is shadowing
#we are creating a new instance attribute based on a aclass attribute

#case study
#a good uise case for class attributes are:
#shared across all instances
#conceptually the same for the whole class
#they are usually configuration like or constant like
#they are counters or class-wide metaata

#bad use cases for class attribute
#values that usally should be different per object.
#any value that changes often or is indivdually different 

#lets look at some examples:
#school name --> class attribute
#max capacity --> class attribute
#account password --> instance attribute
# tax rate --> instance attribute
#course grade --> instance attribute