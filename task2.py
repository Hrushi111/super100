class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed_by = None

    def is_available(self):
        return self.borrowed_by is None

    def borrow(self, member):
        if self.is_available():
            self.borrowed_by = member
            return True
        else:
            return False

    def return_book(self):
        if not self.is_available():
            self.borrowed_by = None
            return True
        else:
            return False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_available_books(self):
        return [book for book in self.books if book.is_available()]


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def borrow_book(self, book):
        return book.borrow(self)

    def return_book(self, book):
        return book.return_book()
        # Create some books
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
        book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
        book3 = Book("1984", "George Orwell", "9780451524935")

        # Create a library
        library = Library()

        # Add books to the library
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        # Create some members
        member1 = Member("John Doe", "M001")
        member2 = Member("Jane Smith", "M002")

        # Member1 borrows a book
        member1.borrow_book(book1)

        # Check if the book is available
        print(book1.is_available())  # False

        # Member2 tries to borrow the same book
        member2.borrow_book(book1)  # Returns False

        # Member1 returns the book
        member1.return_book(book1)

        # Check if the book is available again
        print(book1.is_available())  # True

        # Get all available books in the library
        available_books = library.get_available_books()
        for book in available_books:
            print(book.title)
