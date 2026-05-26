class StudentRecord:
    def __init__(self, name, gpa, credits):
        if not name.strip():
            raise ValueError("NAME CONNOT BE EMPTY")
        self.name = name
        
        self.gpa = gpa
        self.credits = credits
        
#gpa property
@property
def gpa(self):
    return self.__gpa

@gpa.setter
def gpa(self, value):
    if value < 0.0 or value > 4.0:
        raise ValueError("GPA must be between 0.0 and 4.0")
    self.__gpa = value

#credit properties

@property 
def credits(self, value):
    if value < 0:
        raise ValueError("Credits cannot be negative")
    self.__credits = value

#methods
  


