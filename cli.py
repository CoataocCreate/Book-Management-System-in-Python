# cli.py

from book import Book
from database import Database

class BookManagerCLI:
    def __init__(self):
        self.db = Database()

    def run(self):
        while True:
            print("\nBook Management System")
            print("1. Add a new book")
            print("2. Edit a book")
            print("3. Delete a book")
            print("4. Search for a book")
            print("5. List all books")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.edit_book()
            elif choice == "3":
                self.delete_book()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                self.list_books()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        genre = input("Enter genre: ")
        year = int(input("Enter publication year: "))
        book = Book(title, author, genre, year)
        self.db.add_book(book)
        print("Book added successfully.")

    def edit_book(self):
        book_id = int(input("Enter book ID to edit: "))
        # Fetch book details from DB based on book_id, update fields, and save changes

    def delete_book(self):
        book_id = int(input("Enter book ID to delete: "))
        self.db.delete_book(book_id)
        print("Book deleted successfully.")

    def search_book(self):
        query = input("Enter title or author to search: ")
        # Search books by title or author in the DB and display results

    def list_books(self):
        books = self.db.get_all_books()
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}")
        else:
            print("No books found.")

    def __del__(self):
        self.db.close()
