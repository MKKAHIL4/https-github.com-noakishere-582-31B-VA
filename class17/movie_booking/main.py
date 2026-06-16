from core.constants import MAX_TICKETS_PER_BOOKING
from core.enums import ShowStatus
from models.customer import Customer
from models.movie_show import MovieShow
from models.staff import Staff
from core.utils import print_separator, format_title
from models.booking import Booking

def main():

    customer = Customer("Eva Mendez")
    staff = Staff("Micheal Blue", "Manager")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)
    booking = Booking ("Sandra","Silence of the Lamb", 4)
    
    customer.display_info()
    print_separator()
    staff.display_info()
    print_separator()
    show.display_info()
    print_separator()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)
    print_separator()
    booking.display_info()
    

if __name__ == "__main__":
    main()