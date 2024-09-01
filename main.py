#-------------------------------------------Test Cases------------------------------------------------------------------
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




#-------------------------------------- Production Code --------------------------------------------------------------------------