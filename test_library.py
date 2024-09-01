import unittest

from main import Book,Library
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


