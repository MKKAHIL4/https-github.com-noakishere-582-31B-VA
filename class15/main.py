from users import Customer, Staff, VIPCustomer
from movie_show import MovieShow
from enums import ShowStatus


print("======Creating Users ========")

customer1 = Customer("Emkay", "emkay@hotmail.com", "C0001")
staff1 = Staff("micky", "micky@hotmail.com", "E0001")
vip1 = VIPCustomer("James","james@hotmail.com", "V0001")

print("\n =======polymorphism Demo ======")
users = [customer1, staff1, vip1]

for user in users:
    user.display_info()

print("\n =======Valid Movie Show ======")
show = MovieShow("Inception", 10)
show.display_info()

print("\n =======Valid Booking ======")

try:
    show.book_tickets(customer1, 3)
    show.display_info()
except Exception as e:
    print("Error:", e)

print("\n =======Invalid booking: too many tickets ======") 

try:
    show.book_tickets(customer1, 10) 
except Exception as e:
    print("Error:", e) 

print("\n =======Sold Out Senario ======")

try:
    show.book_tickets(customer1, 5)
    show.book_tickets(customer1, 2)
    show.display_info()
except Exception as e:
    print("Error:", e) 
    
print("\n =======booking Sold out show ======")

try:
    show.book_tickets(customer1, 1)
except Exception as e:
    print("Error:", e) 

print("\n =======Cancelled show senario ======")

cancelled_show = MovieShow("Spiderman", 5)
cancelled_show.cancel_show()

try:
    cancelled_show.book_tickets(customer1, 1)
except Exception as e:
    print("Error:", e)  

print("\n =======Invalid Capacity ======")
try:
    bad_show = MovieShow("Invalid Movie", 0)
except Exception as e:
    print("Error:", e)  
    
print("\n =======Invalid Status ======")

try:
    show.status = "OPEN"
except Exception as e:
    print("Error:", e) 
    
print("==========end of the program") 

