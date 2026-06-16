class Staff:
    def __init__(self, name, role="Staff"):
        self.name = name
        self.role = role 
        
    def display_info(self):
        print(f"Staff: {self.name} | Role: {self.role}")
        