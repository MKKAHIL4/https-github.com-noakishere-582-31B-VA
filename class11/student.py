from status import StudentLevel


class Student:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, value):
        
        if not isinstance(value, StudentLevel):
            raise ValueError("level must be a Student level value")
        
        self.__level = value
    
    def display_info(self):
        print(
            f"student: {self.name} | "
            f"level: {self.level.value}"
        )
print("\n ========TESTING Student========")
        
student1 = Student("Alice", StudentLevel.BEGINNER)
student1.display_info()
student2 = Student("MK", StudentLevel.INTERMEDIATE)
student2.display_info()
student3 = Student("Micheal", StudentLevel.ADVANCED)
student3.display_info()
    