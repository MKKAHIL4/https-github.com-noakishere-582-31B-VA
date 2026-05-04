print("---------Homewrok Lab02 MKKAHIL---------")
print("----------------------------------------")
print("--Books Created--Exercise 1 Book Class--")

class Book:
    counter = 0 #counts how many books are being created
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
        Book.counter += 1 #increase with every book that is being created

#create Books
book1 = Book("In For A Penny", "Kathryn R Wall") 
book2 = Book("THE Simple Truth", "David Baldacci") 
book3 = Book("Cocktail Hour Under The Tree Of Forgetfulness", "Alexandra Fuller") 
book4 = Book("The Bridge Of Madison County", "Robert James Waller") 

print("\n Total Books created : ", Book.counter, "Books")
print("\n")

print("---Exercise 2 Student Class--")
print("\n")
class Student:
    school_name = "Vanier College"
    student_count = 0
    
    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade
        
        Student.student_count += 1
    
    def display_info(self):
        print(f"{self.name} studies {self.program} at {Student.school_name}, with a Grade of : {self.grade}.")
        
# Stdents Info 
student1 = Student("Micheal", "Web Development", 73)
student2 = Student("Jennifer","Advanced Programming", 82)
student3 = Student("Rumaysa", "Web Interface", 94)

student1.display_info()    
student2.display_info()    
student3.display_info()    

print("Total Students :", Student.student_count)
print("\n")

print("---Exercise 3 Produuct Class--")
print("\n")
class Product:
    category = "Electronics"
    tax_rate = 0.15
    
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def price_with_tax(self):
        return round(self.price + (self.price * Product.tax_rate), 2)
        
product1 = Product("JlabProEarbuds",95)
product2 = Product("Mouse",34.99)
product3 = Product("Keyboard",63.99)

print("----Products with 15% tax----")
print(product1.name, ": $", product1.price_with_tax())        
print(product2.name, ": $", product2.price_with_tax())        
print(product3.name, ": $", product3.price_with_tax())  

# CHANGING THE TAX RATE INTO 20%      
Product.tax_rate = 0.20
print("\n")
print("----Products with 20% tax----")
print(product1.name, ": $", product1.price_with_tax())        
print(product2.name, ": $", product2.price_with_tax())        
print(product3.name, ": $", product3.price_with_tax())  

print("---Exercise 4 Employee Class--")
print("\n")

class Employee:
    company_name = "TechNova"
    bonus_rate = 0.10
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
        Employee.employee_count += 1
        
    def calculate_bonus(self):
        return self.salary * Employee.bonus_rate
    
    def display_employee(self):
        print(f"{self.name} works at {Employee.company_name}. Salary : {self.salary}. Bonus: {self.calculate_bonus()}")
        
#creating employees info
employee1 = Employee("John", 50000)
employee2 = Employee("Samuel", 20000)
employee3 = Employee("Micheal", 60000)

print("\n ---All Employees---")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

Employee.bonus_rate = 0.20

print("\n ---Employee After bonus rate to (20%)---")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

Employee.bonus_rate = 0.50

print("\n ---Employee After bonus rate to (50%)---")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

Employee.bonus_rate = 0.05

print("\n ---Employee After bonus rate to (5%)---")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()