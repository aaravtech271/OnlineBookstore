class Database:
    def __init__(self):
        self.books = []
        self.customers = []

    def get_books(self):
        return self.books

    def save_book(self, book):
        self.books.append(book)

    def get_customers(self):
        return self.customers

    def save_customer(self, customer):
        self.customers.append(customer)
