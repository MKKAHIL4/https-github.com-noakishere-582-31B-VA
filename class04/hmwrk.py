# =====================
# Class 1 -- Playlist
# =====================
class Playlist:
    def __init__(self, name, song_count=0):
        self.name = name
        self.song_count = song_count

    def add_song(self):
        self.song_count += 1
        print("Added 1 song. Now there are", self.song_count)

    def remove_song(self):
        if self.song_count > 0:
            self.song_count -= 1
            print("Removed 1 song. Now there are", self.song_count)
        else:
            print("No songs to remove")

    def show_info(self):
        print("Playlist:", self.name)
        print("Songs:", self.song_count)


# =====================
# Class 2 -- ShoppingCart
# =====================
class ShoppingCart:
    def __init__(self, owner, item_count=0):
        self.owner = owner
        self.item_count = item_count

    def add_item(self, quantity):
        if quantity > 0:
            self.item_count += quantity
            print("Added", quantity, "items. Now there are", self.item_count)
        else:
            print("Invalid quantity")

    def remove_item(self, quantity):
        if quantity <= self.item_count:
            self.item_count -= quantity
            print("Removed", quantity, "items. Now there are", self.item_count)
        else:
            print("Not enough items")

    def show_cart(self):
        print("Owner:", self.owner)
        print("Items:", self.item_count)


# =====================
# Class 3 -- UserAccount
# =====================
class UserAccount:
    def __init__(self, username, active=False, login_count=0):
        self.username = username
        self.active = active
        self.login_count = login_count

    def activate(self):
        self.active = True
        print("Account activated")

    def deactivate(self):
        self.active = False
        print("Account deactivated")

    def login(self):
        if self.active:
            self.login_count += 1
            print("Logged in. Total logins:", self.login_count)
        else:
            print("Account is not active")

    def show_status(self):
        print("Username:", self.username)
        print("Active:", self.active)
        print("Login count:", self.login_count)


# =====================
# Example Usage
# =====================

p1 = Playlist("My Songs")
p1.add_song()
p1.remove_song()
p1.show_info()

print("-----")

cart = ShoppingCart("Ali")
cart.add_item(3)
cart.remove_item(1)
cart.show_cart()

print("-----")

user = UserAccount("john123")
user.login()
user.activate()
user.login()
user.show_status()