
from app import books
from utils.constants import USER_CHOICE
from utils.utilities import display_ascii_art, clear_console

def print_best_books():
    """_summary_:
    sort the books by rating in descending order and print the top 10

    sorted(books.books, key=lambda x: x.rating * -1)[:10] 
    sorts the books by rating in descending order and returns the top 10 books, -1 is used to sort in descending order
    """
    # best_books = sorted(books.books, key=lambda x: x.rating * -1)[:10]
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)

def print_cheapest_books():
    """_summary_:
    sort the books by price in ascending order and print the top 10
    """
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

books_generator = (x for x in books) # generator object
def print_next_book():
    """_summary_:
    print the next book in the catalogue
    """
    print(next(books_generator))

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book
}

def menu():
    """Display the menu and handle user input"""
    try:
        input_choice = input(USER_CHOICE)
        while input_choice != 'q':
            if input_choice in user_choices:
                user_choices[input_choice]()  # call the function depending on the user input

                # I dont think we need the progress bar here
                # with tqdm(total=1, desc="Processing", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
                #     user_choices[input_choice]()  # call the function depending on the user input
                #     pbar.update(1)
            else:
                print("Please enter a valid choice")
            input_choice = input(USER_CHOICE)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting the application gracefully. Goodbye!")

# Clear the console
clear_console()
display_ascii_art()
menu()
