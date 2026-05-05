#static methods!!!

#whats the concept?
    ##static method belongs to class
    #but it does not use self or cls
    #it's marked with @static method
    
class Student:
    #this method deos not need a specific student object or the class itself
    #but its still related to the student domain
    @staticmethod
    def is_valid_name(name):
        if(len(name.strip()) > 0):
            return True
        else:
            return False
print(Student.is_valid_name("Alice"))
print(Student.is_valid_name(""))

class Helper:
    @staticmethod
    def is_valid_email(email):
        return "@" in email and '.' in email # if @ and . are in email then tru==otherwise its false
    
    @staticmethod
    def is_valid_name(name):
        if(len(name.strip()) > 0):
            return True
        else:
            return False
    @staticmethod
    def format_price(price):
        return f"${price:.2f}" 
       
print(Helper.is_valid_email("test"))
print(Helper.is_valid_email("test@test.com"))
    
class Student:
    def __init__(self,name, email):
        if(Helper.is_valid_email(name)):
            self.name = name
        else:
            return   


class Product:
    def __init__(self, name, price, category):
        if(Helper.is_valid_name(name)):
            self.name = name
        else:
            return
        
        self.price = price
        self.category = category
        
        def show_price(self):
            print(Helper.format_price(self.price))
            
            @staticmethod
            def is_valid_category (category):
                return len(category.strip()) > 0
#it's very common in backend programming to have static methods that are helper functions
#because these will be used all over your code, in a standarized manner.

#intsance methods:
    #no decorator (@something)
    #first parameter: self (Always)
    #works with only one object
    #reads/modifies instance state

#class methods:
    #no decorator (@something)
    #first parameteris cls (Always)
    #works with class level state (class attributes, etc...)
    #often used for alternative constructors or shared behavior
    
#static methods:
# decorator: @staticmethod
#no self cls
#usually used as utility/ helper logic

        