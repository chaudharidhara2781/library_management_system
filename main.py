
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

    def view_available_books(self):

        # list of books that are currently available
        available_books = [book for book in self.books if book.available]
        print("Available books:")

        # showing details of each available book
        for book in available_books:
            print(book)
        return available_books


def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View available books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Add a book
            book_id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_year = int(input("Enter publication year: "))
            new_book = Book(book_id, title, author, publication_year)
            library.add_book(new_book)

        elif choice == '2':
            # Borrow a book
            book_id = int(input("Enter book ID to borrow: "))
            library.borrow_book(book_id)

        elif choice == '3':
            # Return a book
            book_id = int(input("Enter book ID to return: "))
            library.return_book(book_id)

        elif choice == '4':
            # View available books
            library.view_available_books()

        elif choice == '5':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
