from status import CourseStatus, DeliveryMode

MAX_CAPACITY = 60

class Course:
    def __init__(self, title, capacity, status, delivery_mode):
        
        set.title = title 
        
        if capacity <= 0:
            raise ValueError("Capacity must be greater then 0")
        
        if capacity > MAX_CAPACITY:
            raise ValueError(f"Capacity cannot exceed {MAX_CAPACITY}")
        
        self.capacity = capacity
        
        self.status = status
        self.delivery_mode = delivery_mode
#STATUS PROPERTY

@property
def status (self):
    return self.__status

@status.setter
def status(self, value):
    
    if not isinstance(value, CourseStatus):
        raise ValueError("status must be a CourseStatus value")
    self.__status = value

#DELIVERY MODE PROPERTY

@property
def delivery_mode(self):
    return self.__delivery_mode

@delivery_mode.setter
def delivery_mode(self, value):
    
    if not isinstance(value, DeliveryMode):
        raise ValueError("delivery_mode must be a DeliveryMode value")
    self.__delivery_mode = value
        