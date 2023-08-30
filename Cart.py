class Cart:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def calculate_total(self):
        total = 0
        for book in self.books:
            total += book.price
        return total
