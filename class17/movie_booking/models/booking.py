class Booking:
    def __init__(self, customer_name, movie_title, tickets):
        self.customer_name = customer_name
        self.movie_title = movie_title
        self.tickets = tickets
    
    def display_info(self):
        print(f"Booking: {self.customer_name} | Movie: {self.movie_title} | tickets: {self.tickets} tickets")