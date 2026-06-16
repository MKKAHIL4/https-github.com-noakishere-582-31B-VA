from core.constants import MAX_TICKETS_PER_BOOKING
from core.enums import ShowStatus
from models.customer import Customer
from models.movie_show import MovieShow
from models.staff import Staff
from core.utils import print_seperator, format_title

def main():

    customer = Customer("Eva Mendez")
    staff = Staff("Micheal Blue", "Manager")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)

    customer.display_info()
    print_seperator()
    staff.display_info()
    print_seperator()
    show.display_info()
    print_seperator()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)
    
    

if __name__ == "__main__":
    main()