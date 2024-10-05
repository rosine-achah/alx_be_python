class Book:
    def __init__(self, title, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []  


    def add_book(self, book):
        self._books.append(book)


    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()


    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                    

    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
              print(f"{book.title} by {book.author}")

# library = Library()

# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# #print(library.list_available_books(book1, book2, book3)) # Lists all books
# print(library.check_out_book("1984"))  # Checks out "1984"
# #print(library.list_available_books())  # Lists available books after checkout
# print(library.return_book("1984"))     # Returns "1984"
#print(library.list_available_books())