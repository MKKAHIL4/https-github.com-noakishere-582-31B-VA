print("---------Library-item-Tracker Lab MKKAHIL---------")
print("----------------------------------------")
print("-- Book Class--")
class Book:
    
    library_name = "Central Library"
    count = 0 


    def __init__(self, title, author, available = True):
        self.title = title
        self.author = author
        self.available = available 
        
        #increment book count
        Book.count +=1
        
        #instance methods
    def borrow(self):
        if self.available:
            self.available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is not available.")
    
    def return_book(self):
        self.available = True
        print(f"'{self.title}' has been returned.")
    
    def display_info(self):
        if self.available:
            status = "Available"    
        else:
            status = "Not Available"
        print(f"------Book Info-------")
        print("Title: ", self.title)
        print("Author: ", self.author)
        print( "Status: ", status)
        print( "Library: ", Book.library_name)
book1 = Book("100 years of Solitude", "Gabriel Garcia Marquez", True)
book2 = Book("Clean Code", "Robert C. Martin",False)
book3 = Book("Micro economics", "Pearson edition", False)

book1.display_info()
book1.borrow()
book1.display_info()
 
book2.display_info()
book2.borrow()
book2.display_info()
 
book3.display_info()
book3.borrow()
book3.display_info()
               