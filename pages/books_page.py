import re
import logging
from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocators
from parser.book_parser import BookParser

logger = logging.getLogger('scraping.all_books_page')
class BooksPage:
    """_summary_:
    Takes in an HTML page (or part of one), and finds properties of an item in it.
    """
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        logger.debug(f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}`.')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
    
    @property
    def page_count(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        logger.debug('Finding the number of catalogue pages available...')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        logger.debug(f'Found number of catalogue pages available: `{content}`.')
        
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages