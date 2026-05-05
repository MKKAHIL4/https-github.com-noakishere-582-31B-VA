class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("100 years of Solitude", "Gabriel Garcia Marquez", 10.99)
book2 = Book("Clean Code", "Robert C. Martin", 20.99)

print(book1.price)

book1.price = 100.99

print(book1.price)

class Product:
    def __init__(self, name, price, stock = 0):
        self.name = name
        self.price = price
        self.stock = stock
p1 = Product("keyboard", 20, 10)
p2 = Product("Mouse",5)

print(p2.stock)
p2.stock = 100
print(p2.stock) 