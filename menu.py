from app import books

def print_best_books():
    """_summary_:
    sort the books by rating in descending order and print the top 10

    sorted(books.books, key=lambda x: x.rating * -1)[:10] 
    sorts the books by rating in descending order and returns the top 10 books, -1 is used to sort in descending order
    """
    # best_books = sorted(books.books, key=lambda x: x.rating * -1)[:10]
    best_books = sorted(books.books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)



def print_cheapest_books():
    """_summary_:
    sort the books by price in ascending order and print the top 10
    """
    cheapest_books = sorted(books.books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books.books) # generator object
def print_next_book():
    """_summary_:
    print the next book in the catalogue
    """
    print(next(books_generator))


USER_CHOICE = """Enter one of the following

- 'b' to look at the best books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to quit

Enter your choice: """

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book
}

def menu():
    """Display the menu and handle user input"""
    input_choice = input(USER_CHOICE)
    while input_choice != 'q':
        if input_choice in user_choices:
            user_choices[input_choice]()  # call the function depending on the user input
        else:
            print("Please enter a valid choice")
        input_choice = input(USER_CHOICE)

menu()
