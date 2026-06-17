from core.constants import MAX_TICKETS_PER_BOOKING
from core.enums import ShowStatus
from models.customer import Customer
from models.movie_show import MovieShow
from models.staff import Staff
from core.utils import print_separator, format_title
from models.booking import Booking
from core.utils import apply_discount
from core.constants import TICKET_PRICE
from booking import book_ticket, book_ticket_selection, view_bookings



def main():

    customer = Customer("Eva Mendez")
    staff = Staff("Micheal Blue", "Manager")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)
    booking = Booking ("Sandra", "Silence of the Lamb", 4)
    
    total_cost = 3 * TICKET_PRICE
    price = 29.99
    final_price = apply_discount(price, 10)
    
    
    
    customer.display_info()
    print_separator()
    staff.display_info()
    print_separator()
    show.display_info()
    print_separator()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)
    print_separator()
    booking.display_info()
    print_separator()
    print_separator()
    print(f"Original Price: {price}")
    print(f"Discounted price: {final_price}")
    print_separator()
    print_separator()
    print(f"Total ticket cost: {total_cost}")
    3
    print_separator()
    print("\n ===Booking menu===")
    print("1.Original Booking")
    print("2.Movie Selection Booking")
    print("3.View Bookings")
    print("4.Exit")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        book_ticket()
    elif choice == 2: 
        book_ticket_selection()
    elif choice == 3: 
        view_bookings()
    elif choice == 4: 
        print("GoodBye & Thank You!")   
    else:
        print("Invalid choice!!") 
     
     
if __name__ == "__main__":
    main()