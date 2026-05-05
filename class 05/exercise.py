# you are designing a product class
 #product class needs:
 #name
 #price
 #category

 #the data to create this class may arrive in 3 different formats:

 #1. seperate constructor arguments (__init__)
 #2. one comma seprated string
#3. a dictionary

 #you need to design the class so all three formats can be used cleanly

 #example of a dictionary
#example_dict = {
 #    "name" : "something"
  #   "price" : 0,
   #  "category" : "something else"

# }

 #example of comma seperated 
 #ex_str = ""something, 0 something else
 #hint --> int(str) converts a string to an integer
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price 
        self.category = category
        
    #2 create from comma-seprated string

    @classmethod
    def from_string(cls, data_str):
        #split the string
        parts = data_str.split(",")
        
        #clean spaces and assign values
        name = parts[0]
        price = float(parts[1])
        category = parts[2]
        
        return cls(name, price, category)

    #from dictionary
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            data_dict["name"],
            data_dict["price"],
            data_dict["category"],
            
        )
        
    def display(self):
        print("Name", self.name)
        print("Price:", self.price)
        print("Category", self.category)
        print("--------")
p1 = Product("Laptop", 1200, "Electronics")
p1.display()

data = "phone, 800, Electronics"
p2 = Product.from_string(data)
p2.display()

example_dict = {
    "name": "Tablet",
    "price": 500,
    "category": "Electronics"
}

p3 = Product.from_dict(example_dict)
p3.display()

