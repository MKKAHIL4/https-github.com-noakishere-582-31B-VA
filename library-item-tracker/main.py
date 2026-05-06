
from book import Book
print("--Library Items-Books--")

#creating books

book1 = Book("100 years of Solitude", "Gabriel Garcia Marquez", True)
book2 = Book("Clean Code", "Robert C. Martin",False)
book3 = Book("Micro economics", "Pearson edition", False)
#testing-printing initial state 
book1.display_info()
print("\n")
book2.display_info()
print("\n")
book3.display_info()
print("\n")


#borrow books
print("\n -- borrowing books ---")
book1.borrow()
book2.borrow()
book3.borrow()

#show after borrowing
print("\n--displaying after borrowing--")
book1.display_info()
print("\n")
book2.display_info()
print("\n")
book3.display_info()

# class methods
print("\n --change library name--")
print("\n")
Book.change_library_name("Montreal Library")
book1.display_info
print("Library is : ", Book.library_name)
print("\n")

#returning the book
print("\n --Returning Book---")
book1.return_book()
book1.display_info()
print("\n")
book2.return_book()
book2.display_info()
print("\n")
book3.return_book()
book3.display_info()
print("\n")
print("=======")
#SHOW COUNT
print("\n--Total books--")
Book.show_count()

# static method test
print("\n--Title Validation--")
print(Book.is_valid_title("Clean Code"))
print(Book.is_valid_title(""))

#alternative Constructor
print("\n--Create book from String--")
book4 = Book.from_string("Atomic Habits, James Clear, True")
book4.display_info()