class Student:
    school_name = "ABC College"
    
    def __init__(self, name):
        self.name = name
        
        #instance method!
        #here introduce belongs to an instance of class student
    def introduce(self):
            print(f"My name is: {self.name}")
            
student1 = Student("John Doe") 
student2 = Student("Jane Don") 

#introduce here only works with an object
student1.introduce()
student2.introduce()

#Sometimes, we might need a method that changes a class attribute

#we might also need a helper method that checks if everything is valid
#from here we move towards class methods and static methods
#intsnace methods take self and they work with one object

#if we go towards a class method
    #class method works with the class itself
    #it recieves cls instead of self (as a signature)
    #it's also marked @classmethod
class Student:
    school_name = "ABC College"
    
    def __init__(self, name):
        self.name = name
    
    @classmethod # we add the mark
    def show_school(cls): # clas as a signature
        print(f"School: {cls.school_name}")
        
        Student.show_school() # the method is not about specific student!
                   # it is about the whole class!


#compare them directly 
    
    #instance methods: 
                #first parameter : self(ALWAYS!)
                #uses only one object
                
            
                #Class method:
                #forst parameter : class (ALWAYS!) 
                #use the class
                
class Product:
    count = 0
    def __init__(self, name):
          self.name = name
          self.increment_count()
        # Product.count +=1
            
    @classmethod # we add the mark
    def show_count(cls): # clas as a signature
        print(f"School: {cls.count}")
    @classmethod # we add the mark
    def increment_count(cls): # class as a signature
        cls.count += 1
p1 = Product("Mouse")
p2 = Product("Keyboard")
p3 = Product("printer")

Product.show_count()
print(p1.count)
print(p2.count)
print(p3.count)

#lets move owards out frist design pattern

#alternative constructor:
class Student:
    def __init__(self, name, program):
        self.name = name
        self.program = program
    @classmethod
    def from_string(cls, data):
        name, program = data.split(",")
        return cls(name, program)
    
    @classmethod
    def from_form(cls,data):
        #parse the data according to how it's recieved
        pass #ignore this function
    @classmethod 
    def newly_admitted(cls, name):
     return cls(name, "")
student3 = Student("Alice", "Web Development") #valid!
student4 = Student("micheal", "Programming") #valid!
student3 = Student.from_string("Alice,Web Development")
print(f"{student3.name} studies in {student3.program}")
    
#alternative constructor
data = "test,test2"

print(data.split(","))
#in real program, data often comes in a variety of formats
    #for example comma-seperated strings(csv, excel sheet, etc.)
    # a dictionary
    # as a databse row 
    #as a databse row
    #as a JSON object
    #sometimes a user input that needs conversion 
    #so an example if u hve a databse in ur sheet or excel
    #example value1 value 2 value3
    
#alternative 
   
    
    
    
    