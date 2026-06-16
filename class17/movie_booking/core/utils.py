def print_separator(length=20):
    print("-" * length)
    
def format_title(title):
    return title.strip().title

def apply_discount(price, percent):
    return price- (price * percent / 100)
