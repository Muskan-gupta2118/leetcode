#library management 
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available..." if self.available else "Borrowed"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book borrowed successfully.")
                else:
                    print("Book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book returned.")
                return
        print("Book not found.")


library = Library()

library.add_book(Book(101, "Python", "Guido"))
library.add_book(Book(102, "Java", "James"))

library.display_books()

library.borrow_book(101)

library.display_books()

library.return_book(101)

library.display_books()