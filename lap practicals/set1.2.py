class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        """Display book information."""
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}")
        
    def update_author(self, new_author):
        """Update the author's name."""
        self.author = new_author
        print(f"Author of '{self.title}' updated to {self.author}.")


class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book, copies=1):
        """Add a book to the library."""
        self.books.append({'book': book, 'copies': copies})
        print(f"Added '{book.title}' to the library with {copies} copies.")

    def lend_book(self, title):
        """Lend a book if available."""
        for book_entry in self.books:
            if book_entry['book'].title == title and book_entry['copies'] > 0:
                book_entry['copies'] -= 1
                print(f"Book '{title}' has been lent.")
                return
        print(f"Sorry, '{title}' is not available right now.")
        
    def display_available_books(self):
        """Display available books in the library."""
        print("Available books in the library:")
        for book_entry in self.books:
            if book_entry['copies'] > 0:
                print(f"Title: {book_entry['book'].title}, Author: {book_entry['book'].author}, Copies: {book_entry['copies']}")

book1 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
book2 = Book("1984", "George Orwell", "9780451524935")


library = Library()


library.add_book(book1, 3)
library.add_book(book2, 2)


library.display_available_books()


library.lend_book("1984")

library.display_available_books()

book1.update_author("Lee Harper")
book1.display_info()                
