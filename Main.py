from book import Book
from customer import Customer
from cart import Cart
from database import Database

class OnlineBookstore:
    def __init__(self):
        self.books = []
        self.customers = []
        self.database = Database()  # Initialize the database

    def run(self):
        # TODO: Implement the user interface logic here

        # Sample code to demonstrate functionality
        customer = Customer("John Doe", "john@example.com")
        self.customers.append(customer)

        book1 = Book("Book 1", "Author 1", 29.99)
        book2 = Book("Book 2", "Author 2", 19.99)
        self.books.append(book1)
        self.books.append(book2)

        cart = Cart()
        cart.add_book(book1)
        cart.add_book(book2)
        customer.add_to_cart(cart)
        customer.view_cart()

        # Save books and customers to the database
        for book in self.books:
            self.database.save_book(book)
        for customer in self.customers:
            self.database.save_customer(customer)


if __name__ == "__main__":
    bookstore = OnlineBookstore()
    bookstore.run()
