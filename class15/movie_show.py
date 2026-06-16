from enums import ShowStatus
from constants import MAX_TICKETS_PER_BOOKING
from exceptions import (InvalidBookingError, ShowCancelledError, ShowSoldOutError, InvalidStatusError)

class MovieShow:
    #constructor
    def __init__(self, title, capacity):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
     #validate title   
        self.__title = title
    #use property validation
        self.capacity = capacity
        #set initial values
        self.__booked_seats = 0
        self.status = ShowStatus.OPEN
        #property getter capacity
    @property
    def capacity(self):
        return self.__capacity
    #properyt settter with validation
    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.__capacity = value
    #property getter for status    
    @property
    def status(self):
        return self.__status
    #property setter for status validation
    @status.setter
    def status(self, value):
        if not isinstance(value, ShowStatus):
            raise InvalidStatusError("Status must be a showstatus value.")
        self.__status = value
    #read only property that calculates remaining seats
    @property
    def remaining_seats(self):
        return self.__capacity - self.__booked_seats
    
    @property
    def is_full(self):
        return self.remaining_seats == 0
    #book tickets for a customer
    def book_tickets(self, customer, quantity):
        #validate quantity
        if quantity <= 0:
            raise InvalidBookingError("Ticket quantity must be greater than 0.")
        #enforce booking limit
        if quantity > MAX_TICKETS_PER_BOOKING:
            raise InvalidBookingError(f"Cannot book more than " f"{MAX_TICKETS_PER_BOOKING} tickets.")
        #cannot book canceled shows
        if self.__status == ShowStatus.CANCELLED:
            raise ShowCancelledError("Cannot book a cancelled show.")
        #cannot book soldout
        if self.__status == ShowStatus.SOLD_OUT:
            raise ShowSoldOutError("The Show is Sold Out.")
        #ensure enoguh seats remain 
        if quantity > self.remaining_seats:
            raise InvalidBookingError("Not enough seats available.")
        #update booking count
        self.__booked_seats += quantity
        print(f"{customer.name} booked " f"{quantity} tickets.")
        #automatically mark as sold out
        if self.__booked_seats == self.__capacity:
            self.__status = ShowStatus.SOLD_OUT
            #cancel the show
    def cancel_show(self):
        self.__status = ShowStatus.CANCELLED
        
    def reopen_show(self):
        if self.__status == ShowStatus.CANCELLED:
            raise InvalidBookingError("Cancelled shows cannot be reopened")
        
        if self.__status == ShowStatus.SOLD_OUT:
            self.__status = ShowStatus.OPEN
    #display information
    def display_info(self):
        print("\nMovie show Information")
        print("------------------------")
        print(f"Title: {self.__title}")
        print(f"Capacity: {self.__capacity}")
        print(f"Booked Seats: {self.__booked_seats}")
        print(f"Remaining Seats: {self.remaining_seats}")
        print(f"Status: {self.__status.name}")