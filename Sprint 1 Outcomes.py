#Imports
from pyfiglet import Figlet
from rich import print


#Menu Class
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

        while in_progress:
            self.print_line() 
            print("1. View Help")
            print("2. View All Books")
            print("3. Exit")
            self.print_line()
            
            #Menu Navigation
            user_selection = input("Please enter a number between 1 and 3 to navigate the program: ") 
            if user_selection == "1":
                self.view_help()
            elif user_selection == "2":
                self.display_books()
            elif user_selection == "3":
                in_progress = False
            else:
                self.print_line()
                print(f"[red]Please enter a number from 1 to 3.[/red]")
    
    # Help Page
    def view_help(self):
        self.print_line()
        print('''Welcome to CheckMate!

Overview:
CheckMate is an application designed to make searching for books simple and fast. Follow these instructions to navigate the menu:

1. View Help: Display this help message.
   Example: Enter '1' and press Enter.

2. View All Books: Display a list of all available books.
   Example: Enter '2' and press Enter.

3. Exit: Close the application.
   Example: Enter '3' and press Enter.

Navigation Tips:
- Enter the corresponding number for the action you want to take.
- Follow the prompts for additional information when required.

Troubleshooting Tips:
- If you encounter issues, check you are entering the right numbers.
- Check for error messages and refer to this help section for assistance.

Happy reading with CheckMate!
''')

    def display_books(self):
        pass

# Example usage
if __name__ == "__main__":
    menu = Menu()

    while True:
        menu.main_menu()