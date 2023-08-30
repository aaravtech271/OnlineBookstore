class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = None

    def add_to_cart(self, cart):
        self.cart = cart

    def view_cart(self):
        if self.cart:
            print("Cart Contents:")
            for book in self.cart.books:
                print(book)
        else:
            print("Cart is empty.")
