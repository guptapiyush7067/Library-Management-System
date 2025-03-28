
# Library Management System

# Book Operations
class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}")

# Library Class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book ID {book_id} removed successfully.")
                return
        print(f"Book ID {book_id} not found.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display_info()

# Main Code
if __name__ == "__main__":
    lib = Library()

    # Adding books
    book1 = Book(1, "Python Programming", "John Doe", 5)
    book2 = Book(2, "Data Science Essentials", "Jane Smith", 3)

    lib.add_book(book1)
    lib.add_book(book2)

    # Display books
    print("\nAvailable Books:")
    lib.display_books()

    # Remove a book
    lib.remove_book(1)

    # Display books after removal
    print("\nAvailable Books After Removal:")
    lib.display_books()
