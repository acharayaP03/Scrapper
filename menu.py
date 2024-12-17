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


print_best_books()

print("----------- Cheap Books -----------")
print_cheapest_books()
