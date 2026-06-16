# data classes

# data classes' main job is to store and represent data clearly.

from dataclasses import dataclass


# Regular version
class Student:
    def _init_(self, name, gpa):
        self.name = name
        self.gpa = gpa

# Data class version
@dataclass
class Student:
    name: str
    gpa: float

student1 = Student("Alice", 3.8)
student2 = Student("Alice", 3.8)
print(student1)

print(student1 == student2)

# for simple data container, a data class is much cleaner and faster to write

# what does the dataclass give me ??



# auto-generated display

# auto-generated equality function -- to compare different instances/objects

# auto-generated init

# how to have default values for dataclasses

@dataclass
class Course:
    title: str
    credits: int = 3 #defining a default value

course1 = Course("Advanced Programming")
course2 = Course("Phys Ed", 4)

print(course1)
print(course2)



#the class has lots of behaviour
#the class enforces many invariants
#the class has complex property logic
#the class manages state changes heavily

# when is a data class a good fit?

#stores data
#represents a record
#all of this benefits from automatic functions such as _init_, equality with comparisons, etc.

# methods inside a data class
@dataclass
class Product:
name: str
price: float
quantity: int

def total_value(self):
return self.price * self.quantity

product1 = Product("Keyboard", 49.99, 3)

print(product1.total_value()) # dataclass method is called