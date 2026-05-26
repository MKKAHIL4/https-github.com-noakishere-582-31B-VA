class Course_Section:
    def __init_(self, title, capacity, enrolled=0):
        if not title.strip():
            raise ValueError("Ttile cannot be empty")
        self.title = title
        
        self.capacity = capacity
        self.enrolled = enrolled
        
        self.waitlist = 0;
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

    @capacity.setter
    def enrolled(self, value):
        
        if value <= 0:
             raise ValueError("Enrolled students cannot be negative!")
        
        if value > self.capacity:
             raise ValueError("Enrolled students cannot exceed capacity!")
         
        self.__enrolled = value
    
    # waiting list property