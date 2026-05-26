class StudentRecord:
    def __init__(self, name, gpa, credits):
        if not name.strip():
            raise ValueError("NAME CONNOT BE EMPTY")
        self.name = name
        
        self.gpa = gpa
        self.credits = credits
        

