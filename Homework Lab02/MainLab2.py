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
        return self.price + (self.price * Product.tax_rate)
        
product1 = Product("JlabProEarbuds",90)
product2 = Product("Mouse",30)
product3 = Product("Keyboard",60)

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
