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
    