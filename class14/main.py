#exceptions

#raise ValueError("This is not correct")

#number = int("Hello")
#Python cannot convert hello to an integer
#executions fails
#Python raises an exception

#so what is an exception?
#AN exception is an eroor signal that interrupts normal execution.

#something unexpected happened

#normal execution connot continue here *safely*
#not every problem should be handled the same way!

#IMPORTANT: Exceptional situations need to be handled, before they break the code!

# def set_gpa(value):
#     if value < 0 or value > 4:
#         print("Invalid GPA")
        
# this would be weak:
#it signals a problem but doesnt force the caller to handle it
#the program may continue in a bad state 
#the error is easier to ignore

# def set_gpa(value):
#     if value < 0 or value > 4:
#         raise ValueError("Invalid GPA") 
    #now the caller must deal with the problem or the program stops clearly.
    ###this is a better design***

#try, except, else, finally

# basic try/except
# try:
#     number = int(input("Enter A number"))
#     print("you entered : ", number)
# except ValueError:
#     print("That was an invalid integer")
#in this cas, they may fail, and if a matching exception happens, control jumps to except
print("end")    
#in the try/except block above, our code acknowledges if an error is happening but doesn't break/ interrupt our runtime.
#this way the error is handled by the code

try:
    number = int("Hello")
    print("You Entered: ", number)
except ValueError as error: # getting the exception object
    print("Error message: ", error)
    
#this could be useful to inspect or print exception error

try:
    x=int(input("Enter numerator"))
    y=int(input("Enter denominator"))
    division = x / y 
    print(division)
except ValueError:
    print("Please enter a valid integer.!")
except ZeroDivisionError:
    print("You cannot devide by zero")

# else
try: # try to do something
number = int("42")
except ValueError: # raise an exception, in case of an error
print("Conversion failed. ")
else: # if it's successful, do the following:
print("Conversion succeeded: ", number)

# finally block

# else
try: # try to do something
number = int("42")
except ValueError: # raise an exception, in case of an error
print("Conversion failed. ")
else: # if it's successful, do the following:
print("Conversion succeeded: ", number)

# finally block

try: # try to do somthing
    print("Trying .. ")
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"The result is {result}")
finally:
    print("Operation is over. ")

#FINALLY RUNS NO MATTER WHAT!

#the flow is : 
                #try --> if it works --> else
                #if it doesnt work --> excepts
#                                                --> finally
print("=====================")
#Raising exceptions deliberately

#programs should raise exception when they detect invalid situations. when that happens we use raise

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient Funds")
    return balance - amount

# withdraw(1000, 1100)

# Python itself has many built-in exception types, it's up to us to use the one that matches our prob.

# Common ones that we'll use are:
# ValueError
# ZeroDivisionError
# KeyError
# TypeError
# IndexError

#let's move on to exceptions in classes and invariants
class InvalidGPAError(Exception):
    pass
class StudentRecord:
    def __init__(self, name, gpa):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.__name = name
        self.gpa = gpa

    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if not (0.0 <= value <= 4.0):
            raise InvalidGPAError("GPA Must be between 0.0 and 4.0")
        self.__gpa = value
        
sr1 = StudentRecord("Test", 5)

# this is exactly where exceptions become useful in object-oriented design:

# the class protects itself
# invalid states are rejected clearly
# callers must deal with the problem

try:
    sr2 = StudentRecord("Alice", 5.0)
except InvalidGPAError as error:
    print("Could not create student record: ", error)
except ValueError as error:
    print("Could not create student record: ", error)
    