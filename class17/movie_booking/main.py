from core.constants import MAX_TICKETS_PER_BOOKING
from core.enums import ShowStatus
from models.customer import Customer
from models.movie_show import MovieShow
from models.staff import Staff


def main():

    customer = Customer("Ava")
    staff = Staff("Micheal", "Manager")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)

    customer.display_info()
    staff.display_info()
    show.display_info()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)
    
    

if __name__ == "__main__":
    main()