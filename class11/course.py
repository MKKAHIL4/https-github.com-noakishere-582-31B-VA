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
    
        