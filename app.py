

"""_summary_
Books store web scrapper 
"""

import requests
from bs4 import BeautifulSoup
from pages.books_page import BooksPage

page_content = requests.get('http://books.toscrape.com').content

page = BooksPage(page_content)


# will return a list of BookParser objects in __repr__ format
for book in page.books:
    print(book)

# will return a list of BookParser objects in __repr__ format
for book in page.books:
    print(book.name)
    print(book.price)
    print(book.rating)
    print(book.link)
    print()