from enums import ShowStatus
from constants import MAX_TICKETS_PER_BOOKING
from exceptions import (InvalidBookingError, ShowCancelledError, ShowSoldOutError, InvalidStatusError)

class MovieShow:
    def __init__(self, title, capacity):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        
        self.__title = title
        self.capacity = capacity
        self.__booked_seats = 0
        self.status = ShowStatus.OPEN
        
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.__capacity = value
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if not isinstance(value, ShowStatus):
            raise InvalidStatusError("Status must be a showstatus value.")
        self.__status = value
    
    @property
    def remaining_seats(self):
        return self.__capacity - self.__booked_seats
    
    @property
    def is_full(self):
        return self.remaining_seats == 0
    
    def book_tickets(self, customer, quantity):
        if quantity <= 0:
            raise InvalidBookingError("Ticket quantity must be greater than 0.")
        
        if quantity > MAX_TICKETS_PER_BOOKING:
            raise InvalidBookingError(f"Cannot book more than " f"{MAX_TICKETS_PER_BOOKING} tickets.")
        
        if self.__status == ShowStatus.CANCELLED:
            raise ShowCancelledError("Cannot book a cancelled show.")
        
        if self.__status == ShowStatus.SOLD_OUT:
            raise ShowSoldOutError("The Show is Sold Out.")
        
        if quantity > self.remaining_seats:
            raise InvalidBookingError("Not enough seats available.")
        
        self.__booked_seats += quantity
        print(f"{customer.name} booked " f"{quantity} tickets.")
        
        if self.__booked_seats == self.__capacity:
            self.__status = ShowStatus.SOLD_OUT
            
    def cancel_show(self):
        self.__status = ShowStatus.CANCELLED
        
    def reopen_show(self):
        if self.__status == ShowStatus.CANCELLED:
            raise InvalidBookingError("Cancelled shows cannot be reopened")
        
        if self.__status == ShowStatus.SOLD_OUT:
            self.__status = ShowStatus.OPEN
    
    def display_info(self):
        print("\nMovie show Information")
        print("------------------------")
        print(f"Title: {self.__title}")
        print(f"Capacity: {self.__capacity}")
        print(f"Booked Seats: {self.__booked_seats}")
        print(f"Remaining Seats: {self.remaining_seats}")
        print(f"Status: {self.__status.name}")