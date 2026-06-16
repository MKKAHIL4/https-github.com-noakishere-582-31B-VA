from core.enums import ShowStatus

class MovieShow:
    def __init__(self, title, capacity, status):
        self.title = title
        self.capacity = capacity
        self.status = status

    def display_info(self):
        status_text = self.status.value.replace("_", " ").title()
        print(f"Movie: {self.title}") 
        print(f"Capacity: {self.capacity} seats")
        print(f"Status: {status_text}")