class Course_Section:
    def __init__(self, title, capacity, enrolled=0, waitlist=0):
        if not title.strip():
            raise ValueError("Ttile cannot be empty")
        
        self.title = title
        
        self.capacity = capacity
        self.enrolled = enrolled
        
        self.waitlist = waitlist;
    #capacity property
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        
        if value <= 0:
             raise ValueError("Capacity Must be Greater Than 0..!!")
         
        self.__capacity = value
        
    #Enrolled porperty
    
    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, value):
        
        if value < 0:
             raise ValueError("Enrolled students cannot be negative!")
        
        if value > self.capacity:
             raise ValueError("Enrolled students cannot exceed capacity!")
         
        self.__enrolled = value
    
    # waiting list property
    @property
    def waitlist(self):
        return self.__waitlist

    @waitlist.setter
    def waitlist(self, value):
        
        if value < 0:
             raise ValueError("Waiting list cannot be negative!")
         
        self.__waitlist= value
    
    #methods
    def register_student(self):
        
        if self.__enrolled >= self.__capacity:
            raise ValueError("Course is full")
        
        self.__enrolled += 1 
    
    def drop_student(self):
        if self.__enrolled <= 0:
            raise ValueError("No students to drop")
        
        self.__enrolled -= 1 
        
    #waitlist methods
    
    def add_to_waitlist(self):
        self.waitlist += 1
    
    def remove_from_wailist(self):
        if self.__waitlist <= 0:
            raise ValueError("waitlist is empty")
        
        self.__waitlist -= 1 
        
    def display_info(self):
        print(f"Course: {self.title}")
        print(f"Cpacity: {self.capacity}")
        print(f"Enrolled: {self.enrolled}")
        print(f"Waitlist: {self.waitlist}")
    
course = Course_Section("Physics101", 20, 15, 4)

course.display_info()