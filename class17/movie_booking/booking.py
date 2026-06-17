from core.exceptions import InvalidBookingError
from models.booking import Booking

def book_ticket():
    try:
        customer_name = input("Enter name: ")
        movie_title = input("Enter Movie: ")
        tickets = int(input("Enter tickets:"))
        
        if tickets <= 0 or tickets >= 20:
            raise InvalidBookingError("Seats must be greater than 0 and less than 20 tickets only!!! ")
        booking = Booking(customer_name, movie_title, tickets)
        booking.display_info()
        
        #saving the data entry into a file
        with open("class17/movie_booking/bookings.txt", "a") as file:
            file.write(f"{customer_name}, {movie_title}, {tickets}\n")
        print ("Booking saved Successfully...")   
    except ValueError:
        print("Invalid  Number Input..please try again!!!!")
        
    except InvalidBookingError as e:
        print("Booking error: ", e)