class User:
    def __init__(self, username, email, password_hash):
        self.username = username
        self.__email = email
        self.__password_hash = password_hash

# which attributes are public? which are intended for internal use?
#username - can be accessed directly outside the class
#email, password hash intend for internal use only __ helps protect the data from bieng modified directly outside the class

# 2. redesign the following class to improve encapsulation
class Course:
    def __init__(self, title, seats):
        self.title = title
        self.__seats = seats

# add seats
    def add_seats(self,amount):
        self.__seats += amount
        print(f"{amount} seats added.")

    #remove seats
    def remove_seats(self, amount):
        if amount <= self.__seats:
            self.__seats -= amount
            print(f"{amount} seats removed.")
        else:
            print("not enough seats available.")

    #display
    def show_seats(self):
        print(f"Available seats :{self.__seats} .")

course1 = Course("Canadians Game", 30)

course1.show_seats()
course1.remove_seats(5)
course1.show_seats()

# 3. Create StudentAccount class:

# public username
# internal __credits
# methods: add_credits() - use_credits() - show_credits()
class StudentAccount:
    def __init__(self, username, credits):
        self.username = username
        self.__credits = credits
        
# add seats
    def add_credits(self,amount):
        self.__credits += amount
        print(f"{amount} credits added.")

    #remove seats
    def use_credits(self, amount):
        if amount <= self.__credits:
            self.__credits -= amount
            print(f"{amount} credits used.")
        else:
            print("not enough credits.")

    #display
    def show_credits(self):
        print(f"{self.username} has {self.__credits} credits.")

student1 = StudentAccount("Mike", 100)

student1.show_credits()
student1.add_credits(50)
student1.use_credits(30)
student1.show_credits()


# 4. Create a MovieTicket class:

# public movie_title
# internal available_seats
# methods: book_seat() - cancel_seat() - show_status()

class MovieTicket:
    def __init__(self, movie_title, available_seats):
        self.movie_title = movie_title
        self.__available_seats = available_seats
        
#book seat
    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            print("1 seat booked successfully.")
        else:
            print("No seats Available.")
            
    #cancel seat
    def cancel_seat(self):
        self.__available_seats -= 1
        print("1 seat canceled.")

    def show_status(self):
        print(f"Movie: {self.movie_title}")
        print(f"Available seats: {self.__available_seats}")
    
ticket1 = MovieTicket("Avengers", 7)
ticket1.show_status()
ticket1.book_seat()
ticket1.book_seat()
ticket1.show_status()
ticket1.cancel_seat()
ticket1.show_status()