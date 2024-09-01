# -------------------------------------------Test Cases------------------------------------------------------------------
import unittest


class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Create a library instance before each test case
        self.library = Library()

        # Create some book instances
        self.book = Book(1, "It Ends With Us", "Colleen Hoover", 2016)
        self.book1 = Book(2, "It Starts With Us", "Colleen Hoover", 2022)
        self.book2 = Book(3, "The Lean Startup", "Eric Ries", 2011)

        # Add books to the library
        self.library.add_book(self.book)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        # testing add book function
        book3 = Book(4, "Zero to One", "Peter Thiel", 2014)
        self.library.add_book(book3)
        self.assertIn(book3, self.library.books)

        # test adding duplicate book
        self.library.add_book(self.book1)
        self.assertEqual(len(self.library.books), 4)  # duplicate book not added

    def test_borrow_book(self):
        # testing borrow book
        self.assertTrue(self.library.borrow_book(1))
        self.assertFalse(self.book.available)
        self.assertEqual(len(self.library.books), 3)

        # test borrowing the same book again
        self.assertFalse(self.library.borrow_book(1))

        # test borrowing the book that does not exist
        self.assertFalse(self.library.borrow_book(27))

    def test_return_book_success(self):
        # borrow a book first
        self.library.borrow_book(1)

        # test returning a book
        self.assertTrue(self.library.return_book(1))
        self.assertTrue(self.book1.available)

        # returning an already returned book
        self.assertFalse(self.library.return_book(1))

        # returning a book that does not exist
        self.assertFalse(self.library.return_book(27))

    def test_view_available_books(self):
        # all the available book
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 3)

        # Borrow a book and check available books
        self.library.borrow_book(1)
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 2)

        # Return the book and check available books again
        self.library.return_book(1)
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 3)


# -------------------------------------- Production Code --------------------------------------------------------------------------

class Book:

    # initializing the book object
    def __init__(self, id, title, author, publication_year):
        self.id = id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = True

    def __repr__(self):
        # readable string representation of book obj
        return f"Book({self.id}, '{self.title}', '{self.author}', {self.publication_year}, Available: {self.available})"


class Library:

    # initializing library obj with empty list of book
    def __init__(self):
        self.books = []

    # testcase for add_book feature
    def add_book(self, book):

        # checking for duplicate book
        if any(existing_book.id == book.id for existing_book in
               self.books):  # not adding book if the same book does not exist
            print("Book already exists in the library.")
        else:
            self.books.append(book)
            print(f"Book '{book.title}' added to the library.")  # adding book if no same book added

    # testcase for borrowing a book
    def borrow_book(self, book_id):
        for book in self.books:
            # borrowing a book and marking it as not available
            if book.id == book_id and book.available:
                book.available = False  # marked as not available
                print(f"Book '{book.title}' has been borrowed.")
                return True
        print("Book not available or not found.")
        return False

    def return_book(self, book_id):
        # returning a borrowed book to library and setting it as available
        for book in self.books:
            if book.id == book_id:
                if not book.available:  # Check if the book was borrowed
                    book.available = True  # marked as available/ returned
                    print(f"Book '{book.title}' has been returned.")
                    return True
                else:
                    print(
                        f"Book '{book.title}' was not borrowed.")  # print if user tried to return a book that was not borrowed
                    return False
        print("Book not found in the library.")
        return False

    def view_available_books(self)

        # list of books that are currently available
        available_books = [book for book in self.books if book.available]
        print("Available books:")

        # showing details of each available book
        for book in available_books:
            print(book)
        return available_books
