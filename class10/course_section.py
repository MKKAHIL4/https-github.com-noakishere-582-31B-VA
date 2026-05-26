class Course_Section:
    def __init_(self, title, capacity, enrolled=0):
        if not title.strip():
            raise ValueError("Ttile cannot be empty")
        self.title = title
        
        self.capacity = capacity
        self.enrolled = enrolled
        
        self.waitlist = 0;
    