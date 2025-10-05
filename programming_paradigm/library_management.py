class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

        
    @property
    def is_checked_out(self):
        return self.__is_checked_out

    @is_checked_out.setter
    def is_checked_out(self, value):
        self.__is_checked_out = value
    
class Library:
    def __init__(self):
        self.__books = []

    @property
    def books(self):
        return self.__books

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title and not book.is_checked_out:
                book._is_checked_out = True
                return f"You have checked out '{title}'."
        return f"Sorry, '{title}' is not available."
    
    def return_book(self):
        for book in self.__books:
            if book.title == book.title and book.is_checked_out:
                book.is_checked_out = False
                return f"You have returned '{book.title}'."
        return f"'{book.title}' was not checked out."

    def list_available_books(self):
        available_books = [book.title for book in self.__books if not book.is_checked_out]
        return available_books if available_books else "No books are currently available."