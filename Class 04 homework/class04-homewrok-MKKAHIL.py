# ------Class1-Playslist----------
print("Playlist class01")
class Playlist:
    def __init__(self, name, song_count = 0):
        self.name = name
        self.song_count = song_count
    
    def add_song(self):
        self.song_count += 1
        print("Added one song. now there are", self.song_count)
        
    def remove_song(self):
        if self.song_count > 0:
            self.song_count -= 1
            print("One song was removed. After removing it, now there are", self.song_count, "Songs")
        else:
            print("No songs to remove") 
    
    def show_info(self):
        print("Playlist: ", self.name)
        print("Songs: ", self.song_count)
        
p1 = Playlist("My Songs")
p1.add_song()
p1.add_song()
p1.add_song()

p1.remove_song()

p1.show_info()

print("-----end of class 01 playlist")
print("=======================================")

#class02 Shopping Cart
print("shopping cart class 02")
print("----------------------")
class ShoppingCart:
    def __init__(self, owner, item_count = 0):
            self.owner = owner
            self.item_count = item_count
    def add_item(self, quantity):
        if quantity > 0:
            self.item_count += quantity
            print("Added", quantity, "item in cart. Now there are", self.item_count, "items in cart")
        else:
            print("Invalid quantity")
            
    def remove_item(self, quantity):
        if quantity <= self.item_count:
            self.item_count -= quantity
            print("Removed", quantity, "items from cart. Now there are ", self.item_count, "items in cart")
        else:
            print("No items, Not enough items")
    def show_cart(self):
        print("Owner: ", self.owner)
        print("items: ", self.item_count) 
        
cart = ShoppingCart("Emkay")
cart.add_item(5)
cart.remove_item(2)
cart.show_cart()

print("-----end of class 02 Shopping cart")
print("=======================================")
#class03 UserAccount
print("User Account class 03")
print("---------------------")

class UserAccount:
    def __init__(self, username, active=False, login_count=0):
        self.username = username
        self.active = active
        self.login_count  = login_count
        
    def activate(self):
        self.active = True
        print("Account Activated")
    
    def deactivate(self):
        self.active = False
        print("Account Deactivated")
    
    def login(self):
        if self.active:
            self.login_count += 1
            print("Logged in. The Total Logins: ", self.login_count)
        else:
            print("Account is not Active..")
    def show_status(self):
        print("UserName: ", self.username)
        print("Active: ", self.active)
        print("LOGIN Count: ", self.login_count)
        
user = UserAccount("Emkay1246")
user.login()    
user.activate()    
user.login()    
user.show_status() 
print("=======================================")   
print("-----end of class 03 User Account")
print("=======================================")