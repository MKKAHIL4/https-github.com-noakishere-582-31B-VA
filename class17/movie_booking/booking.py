from core.exceptions import InvalidBookingError
from models.booking import Booking

def book_ticket():
    try:
        customer_name = input("Enter name: ")
        movie_title = input("Enter Movie: ")
        tickets = int(input("Enter tickets:"))
        
        if tickets <= 0 or tickets > 20:
            raise InvalidBookingError("Seats must be greater than 0 and less than 20 tickets only!!! ")
        booking = Booking(customer_name, movie_title, tickets)
        booking.display_info()
        
        #saving the data entry into a file
        with open("class17/movie_booking/bookings.txt", "a") as file:
            file.write(f"Customer name: {customer_name} || Movie Title: {movie_title} || Tickets amount: {tickets}\n")
        print ("Booking saved Successfully...")   
    except ValueError:
        print("Invalid  Number Input..please try again!!!!")
        
    except InvalidBookingError as e:
        print("Booking error: ", e)
        
def book_ticket_selection():
    try:
        customer_name = input("Enter name: ")

        movies = [
            "Silence of the Lamb",
            "Fast and Furious",
            "The Italian Job",
            "The Score"
        ]
        print("\n Available Movies:") 
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie}")
        choice = int(input("Select A Movie: "))
        
        if choice < 1 or choice > len(movies):
            raise InvalidBookingError("Invalid Movie selection!!please try again..!!")    
        movie_title = movies[choice - 1]
        
        tickets = int(input("Enter tickets amount: "))
        
        if tickets <= 0 or tickets > 20:
            raise InvalidBookingError("You can Book 1 0r 20 tickets only")
        
        booking = Booking(customer_name, movie_title, tickets)
        booking.display_info()
        
        with open("class17/movie_booking/bookings.txt", "a") as file:
             file.write(f"Customer name: {customer_name} || Movie Title: {movie_title} || Tickets amount: {tickets}\n")
             print ("Booking selection saved Successfully...")
    except ValueError:
        print("Invalid  Number Input..please try again!!!!")
        
    except InvalidBookingError as e:
        print("Booking error: ", e)       
        
        
def view_bookings():
    try:
        with open("class17/movie_booking/bookings.txt", "r") as file:
            print("\n=====All Bookings ======")
            
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if"||" not in line:
                    print("Skipping invalid line:", line)
                    continue
                parts = line.split("||")
                if len(parts) != 3:
                    print("skipping corrupted line:", line)
                customer_name = parts[0].split(":")[1].strip() 
                movie_title = parts[1].split(":")[1].strip() 
                tickets = parts[2].split(":")[1].strip() 
                   
                
                print(f"Customer: {customer_name}") 
                print(f"Movie: {movie_title}") 
                print(f"Tickets: {tickets}") 
                print("==========================") 
    except FileNotFoundError:
        print("No bookings found yet.")