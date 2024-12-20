import re
import logging  
from locators.books_locators import BookLocators


logger = logging.getLogger('scraping.book_parser')
class BookParser:
    """_summary_:
    A class to take in an HTML page (or part of one), and find properties of an item in it.
    """
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, {self.price}, ({self.rating} stars)>'

    @property
    def name(self):
        """_summary_
        
        Returns:
            _type_: _description_
        """
        locator = BookLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator)
        item_name = item_name.attrs['title']
        return item_name

    @property
    def link(self):
        """_summary_
        
        Returns:
            _type_: _description_
        """
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator)
        item_link = item_link.attrs['href']
        return item_link

    @property
    def price(self):
        """_summary_
        
        Returns:
            _type_: _description_
        """
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        price_string = re.sub(r'[^\d.]', '', item_price.string)
        return float(price_string)

    @property
    def rating(self):
        """_summary_
        
        Returns:
            _type_: _description_
        """
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating = BookParser.RATINGS.get(rating_classes[0])
        return rating

