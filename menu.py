
from app import books
from tabulate import tabulate
from utils.constants import USER_CHOICE
from utils.utilities import display_ascii_art, clear_console, truncate_title, get_exchange_rate, convert_price, get_currency_info


# Global variable to store the user's currency code
USER_CURRENCY = None
USER_CURRENCY_INFO = {}

def print_best_books():
    """_summary_:
    sort the books by rating in descending order and print the top 10

    sorted(books.books, key=lambda x: x.rating * -1)[:10] 
    sorts the books by rating in descending order and returns the top 10 books, -1 is used to sort in descending order
    """
    # best_books = sorted(books.books, key=lambda x: x.rating * -1)[:10]
    exchange_rate = get_exchange_rate("GBP", USER_CURRENCY)
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    table = [
        [truncate_title(book.name), book.rating, f"{USER_CURRENCY_INFO['symbol']} {convert_price(book.price, exchange_rate):.2f}"] for book in best_books
    ]
    print(tabulate(table, headers=["Title", "Rating", "Price"], tablefmt="fancy_grid"))


def print_cheapest_books():
    """_summary_:
    sort the books by price in ascending order and print the top 10
    """
    exchange_rate = get_exchange_rate("GBP", USER_CURRENCY)
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    table = [[truncate_title(book.name), book.rating, f"{USER_CURRENCY_INFO['symbol']} {convert_price(book.price, exchange_rate):.2f}"] for book in cheapest_books]
    print(tabulate(truncate_title(table), headers=["Title", "Rating", "Price"], tablefmt="fancy_grid"))


books_generator = (x for x in books) # generator object
def print_next_book():
    """_summary_:
    print the next book in the catalogue
    """
    exchange_rate = get_exchange_rate("GBP", USER_CURRENCY)
    book = next(books_generator)
    table = [[truncate_title(book.name), book.rating, f"{USER_CURRENCY_INFO['symbol']} {convert_price(book.price, exchange_rate):.2f}"]]
    print(tabulate(table, headers=["Title", "Rating", "Price"], tablefmt="grid"))


def set_user_currency():
    """Prompt the user to set their currency code and store the information."""
    global USER_CURRENCY, USER_CURRENCY_INFO

    USER_CURRENCY = input("Enter your currency code (e.g., USD, EUR): ").upper()
    USER_CURRENCY_INFO = get_currency_info(USER_CURRENCY)
    print(f"Selected currency: {USER_CURRENCY_INFO['country']} ({USER_CURRENCY}) - {USER_CURRENCY_INFO['symbol']}")


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book
}

def menu():
    """Display the menu and handle user input"""
    global USER_CURRENCY

    if USER_CURRENCY is None:
        set_user_currency()
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
