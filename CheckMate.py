# Imports
from pyfiglet import Figlet
from rich import print
import json
import os
import hashlib

# Book Class
class Book:
    def __init__(self, title, author, book_id, available=True):
        # Initialize a Book object with title, author, book_id, and availability status.
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = available    

# LibraryFunctions Class
class LibraryFunctions:
    def __init__(self, library_file='library.json'):
        # Initialize the LibraryFunctions object with the path to the library file.
        self.library_file = library_file
        self.books = self.load_library()

    def load_library(self):
        # Load the library data from the JSON file and create Book objects.
        if os.path.exists(self.library_file):
            with open(self.library_file, 'r') as file:
                book_data = json.load(file)
                return [Book(**book) for book in book_data]
        else:
            return []

    def save_library(self):
        # Save the current state of the library to the JSON file.
        book_data = [{'title': book.title, 'author': book.author, 'book_id': book.book_id, 'available': book.available}
                     for book in self.books]
        with open(self.library_file, 'w') as file:
            json.dump(book_data, file, indent=2)

    def generate_book_id(self, data):
        # Generate a unique book ID based on the SHA256 hash of the provided data.
        sha256_hash = hashlib.sha256(data.encode()).hexdigest()
        return sha256_hash[:6] 

    def add_book(self, title, author):
        # Add a new book to the library with the given title and author.
        if not (1 <= len(title) <= 50) or not (1 <= len(author) <= 50):
            print(f"[red]Invalid title or author length. Title and author must be between 1 and 50 characters.[/red]")
            return
        book_id = self.generate_book_id(title + author)
        new_book = Book(title, author, book_id)
        self.books.append(new_book)
        self.save_library()
        print(f"[green]Book added successfully. ID: {book_id}[/green]")

    def remove_book(self, book_id):
        # Remove a book from the library based on its ID.
        book_found = next((book for book in self.books if book.book_id == book_id), None)

        if book_found:
            self.books = [book for book in self.books if book.book_id != book_id]
            self.save_library()
            print(f"[green]Book with ID {book_id} removed successfully.[/green]")
        else:
            print(f"[red]Error: Book with ID {book_id} not found.[/red]")

    def search_by_id(self, book_id):
        # Search for a book in the library based on its ID.
        book = next((b for b in self.books if b.book_id == book_id), None)

        if book:
            return book
        else:
            print("[red]Error: Book not found.[/red]")
            return None

    def display_books(self):
        # Display the details of all books in the library.
        print(f"{'ID':<10}{'Title':<50}{'Author':<50}{'Available':<10}")
        print("=" * 120)
        for book in self.books:
            print(f"{book.book_id:<10}{book.title:<50}{book.author:<50}{book.available:<10}")

    def check_out_book(self):
        # Check out a book from the library by updating its availability status.
        book_id = input("Enter the ID of the book to check out: ")
        book = self.search_by_id(book_id)

        if book:
            if book.available:
                book.available = False
                self.save_library()
                print(f"[green]Book with ID {book_id} checked out successfully.[/green]")
            else:
                print(f"[red]Error: Book with ID {book_id} is already checked out.[/red]")
        else:
            print(f"[red]Error: Book with ID {book_id} not found.[/red]")

    def return_book(self, book_id):
        # Return a checked-out book to the library by updating its availability status.
        book = self.search_by_id(book_id)

        if book:
            if not book.available:
                book.available = True
                self.save_library()
                print(f"[green]Book with ID {book_id} returned successfully.[/green]")
            else:
                print(f"[red]Error: Book with ID {book_id} is already available.[/red]")
        else:
            print(f"[red]Error: Book with ID {book_id} not found.[/red]")

# Menu Class
class Menu:
    def print_line(self):
        # Print a line of dashes for visual separation.
        print('-' * 50, end='\n')

    def title_text(self):
        # Display the CheckMate title in a stylized format.
        slanted_text = Figlet(font='slant').renderText('CheckMate')
        coloured_text = f"[blue]{slanted_text}[/blue]"
        print(coloured_text)

    def main_menu(self):
        # Display the main menu and handle user input for navigation.
        in_progress = True
        self.title_text()

        library_functions = LibraryFunctions()

        while in_progress:
            self.print_line()
            print("1. View Help")
            print("2. View All Books")
            print("3. Search Books")
            print("4. Add a New Book")
            print("5. Remove a Book")
            print("6. Check Out a Book")
            print("7. Return a Book")
            print("8. Exit CheckMate")
            self.print_line()
            
            user_selection = input("Please enter a number between 1 and 8 to navigate the program: ")

            if user_selection == "1":
                self.view_help()
            elif user_selection == "2":
                library_functions.display_books()
            elif user_selection == "3":
                book_id = input("Enter the ID of the book: ")
                result = library_functions.search_by_id(book_id)
                if result:
                    print(f"Book found: ID: {result.book_id}, Title: {result.title}, Author: {result.author}")
            elif user_selection == "4":
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                library_functions.add_book(title, author)
            elif user_selection == "5":
                book_id = input("Enter the ID of the book to remove: ")
                library_functions.remove_book(book_id)
            elif user_selection == "6":
                library_functions.check_out_book()
            elif user_selection == "7":
                book_id = input("Enter the ID of the book to return: ")
                library_functions.return_book(book_id)
            elif user_selection == "8":
                in_progress = False
            else:
                self.print_line()
                print(f"[red]Please enter a number from 1 to 8.[/red]")

    def view_help(self):
        # Display a help message explaining how to use the CheckMate application.
        self.print_line()
        print('''Welcome to CheckMate!

Overview:
CheckMate is an application designed to make searching for books simple and fast. Follow these instructions to navigate the menu:

1. View Help: Display this help message.
   Example: Enter '1' and press Enter.

2. View All Books: Display a list of all available books.
   Example: Enter '2' and press Enter.

3. Search Books: Allows a user to search for any book using its unique ID.
    Example: Enter '3' and press Enter. Follow the prompts to enter the ID of the book to search.

4. Add a New Book: Add a new book to the library.
   Example: Enter '4' and press Enter. Follow the prompts to enter the title and author.

5. Remove a Book: Remove a book from the library.
   Example: Enter '5' and press Enter. Follow the prompts to enter the ID of the book to remove.

6. Check Out a Book: Check out a book from the library.
   Example: Enter '6' and press Enter. Follow the prompts to enter the ID of the book to check out.

7. Return a Book: Return a book to the library.
   Example: Enter '7' and press Enter. Follow the prompts to enter the ID of the book to return.

8. Exit CheckMate: Exit the application.
   Example: Enter '8' and press Enter.

Navigation Tips: 
- Enter the corresponding number for the action you want to take.
- Follow the prompts for additional information when required.

Troubleshooting Tips:
- If you encounter issues, check you are entering the right numbers.
- Check for error messages and refer to this help section for assistance.

Happy reading with CheckMate!
''')

if __name__ == "__main__":
    menu = Menu()

    while True:
        menu.main_menu()