print("---------Library-item-Tracker Lab MKKAHIL---------")
print("----------------------------------------")
print("--------- Book Class---------")
print("\n")
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
            
        
        # print(f"--Book Info--")
        # print("Title:", self.title)
        # print("Author:", self.author)
        # print("Status:", status)
        # print("Library:", Book.library_name)
        
        #modify display info
        #print(f"{self.title} | {self.author} | {status} | {Book.library_name}")
        
        #modiy display info style in feature branch
        print(f"--Book Info--")
        print(f"Title:  {self.title}")
        print(f"Author:  {self.author}")
        print(f"Status:  {status}")
        print(f"Library:  {Book.library_name}")        
#class methods
    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

    @classmethod
    def show_count(cls):
        print("Total books created: ", cls.count)

    @classmethod
    def from_string(cls, data):
        title, author, available = data.split(",")
        return cls(title.strip(), author.strip(), available.strip() == "True")


#static method

    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and len(title.strip()) > 0 




        
