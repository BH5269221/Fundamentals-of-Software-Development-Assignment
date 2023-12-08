# Imports
from pyfiglet import Figlet
from rich import print
import json
import os
import hashlib

# Book Class
class Book:
    def __init__(self, title, author, book_id, available=True):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = available    

# LibraryFunctions Class
class LibraryFunctions:
    def __init__(self, library_file='library.json'):
        self.library_file = library_file
        self.books = self.load_library()

    def load_library(self):
        if os.path.exists(self.library_file):
            with open(self.library_file, 'r') as file:
                book_data = json.load(file)
                return [Book(**book) for book in book_data]
        else:
            return []

    def save_library(self):
        book_data = [{'title': book.title, 'author': book.author, 'book_id': book.book_id, 'available': book.available}
                     for book in self.books]
        with open(self.library_file, 'w') as file:
            json.dump(book_data, file, indent=2)

    def generate_book_id(self, data):
        sha256_hash = hashlib.sha256(data.encode()).hexdigest()
        return sha256_hash[:6] 

    def add_book(self, title, author):
        if not (1 <= len(title) <= 50) or not (1 <= len(author) <= 50):
            print(f"[red]Invalid title or author length. Title and author must be between 1 and 50 characters.[/red]")
            return
        book_id = self.generate_book_id(title + author)
        new_book = Book(title, author, book_id)
        self.books.append(new_book)
        self.save_library()
        print(f"[green]Book added successfully. ID: {book_id}[/green]")

    def remove_book(self, book_id):
        book_found = next((book for book in self.books if book.book_id == book_id), None)

        if book_found:
            self.books = [book for book in self.books if book.book_id != book_id]
            self.save_library()
            print(f"[green]Book with ID {book_id} removed successfully.[/green]")
        else:
            print(f"[red]Error: Book with ID {book_id} not found.[/red]")

    def search_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return f"[red]Book not found.[/red]"

    def display_books(self):
        print(f"{'ID':<10}{'Title':<50}{'Author':<50}{'Available':<10}")
        print("=" * 120)
        for book in self.books:
            print(f"{book.book_id:<10}{book.title:<50}{book.author:<50}{book.available:<10}")

# Menu Class
class Menu:

    def print_line(self):
        print('-' * 50, end='\n')

    def title_text(self):
        slanted_text = Figlet(font='slant').renderText('CheckMate')
        coloured_text = f"[blue]{slanted_text}[/blue]"
        print(coloured_text)

    def main_menu(self):
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
            1036c5
            user_selection = input("Please enter a number between 1 and 7 to navigate the program: ")

            if user_selection == "1":
                self.view_help()
            elif user_selection == "2":
                library_functions.display_books()
            elif user_selection == "3":
                library_functions.search_by_id()
            elif user_selection == "4":
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                library_functions.add_book(title, author)
            elif user_selection == "5":
                book_id = input("Enter the ID of the book to remove: ")
                library_functions.remove_book(book_id)
            elif user_selection == "6":
                pass
            elif user_selection == "7":
                pass
            elif user_selection == "8":
                in_progress = False
            else:
                self.print_line()
                print(f"[red]Please enter a number from 1 to 8.[/red]")

    def view_help(self):
        self.print_line()
        print('''Welcome to CheckMate!

Overview:
CheckMate is an application designed to make searching for books simple and fast. Follow these instructions to navigate the menu:

1. View Help: Display this help message.
   Example: Enter '1' and press Enter.

2. View All Books: Display a list of all available books.
   Example: Enter '2' and press Enter.

3. Search Books: Not implemented yet.

4. Add a New Book: Add a new book to the library.
   Example: Enter '4' and press Enter. Follow the prompts to enter the title and author.

5. Remove a Book: Remove a book from the library.
   Example: Enter '5' and press Enter. Follow the prompts to enter the ID of the book to remove.

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