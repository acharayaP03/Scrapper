from bs4 import BeautifulSoup
from locators.all_books_page import AllBooksPageLocators
from parser.book_parser import BookParser
class BooksPage:
    """_summary_:
    Takes in an HTML page (or part of one), and finds properties of an item in it.
    """
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]