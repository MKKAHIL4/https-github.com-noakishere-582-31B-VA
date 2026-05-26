from status import CourseStatus, DeliveryMode

MAX_CAPACITY = 60

class Course:
    def __init__(self, title, capacity, status, delivery_mode):
        
        self.title = title 
        
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        
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

    #METHODS

    def close_registration(self):
        self.status = CourseStatus.CLOSED

    def cancel_course(self):
        self.status = CourseStatus.CANCELED
        
    #challenge
    def reopen_course(self):
        if self.status == CourseStatus.CANCELED:
            raise ValueError("Canceled courses can't reopen directly")
        
        if self.status == CourseStatus.CLOSED:
            self.status = CourseStatus.OPEN
            
    def is_open_for_registration(self):
        
        return self.status == CourseStatus.OPEN


    #Display

    def display_info(self):
            print(
                f"title: {self.title} | "
                f"Capacity : {self.capacity} | "
                f"Status : {self.status.value} | "
                f"Delivery Mode : {self.delivery_mode.value} | "
                ) 
print("\n========Testing Course=========== ")   
course1 = Course("Physics 101 ", 10, CourseStatus.OPEN, DeliveryMode.ONLINE)
course1.display_info() 
course2 = Course("Physics 102 ", 20, CourseStatus.CANCELED, DeliveryMode.IN_PERSON)
course2.display_info() 
course3 = Course("Physics 103 ", 30, CourseStatus.CLOSED, DeliveryMode.HYBRID)
course3.display_info() 