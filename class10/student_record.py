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
    def credits(self):
        return self.__credits
        
    @credits.setter
    def credits(self, value):
        if value < 0:
            raise ValueError("Credits cannot be negative")
        self.__credits = value

    #methods
    def add__credits(self, amount):
        if amount < 0:
            raise ValueError("connot add negative credits")
        self.__credits += amount
        
    def update_gpa(self, value):
        
        self.gpa = value

    def display_info(self):
        print(f"student: {self.name}, has a Gpa of: {self.gpa} and Credits: {self.credits}")
    
student = StudentRecord("MK", 3.5, 15)

student.display_info()

