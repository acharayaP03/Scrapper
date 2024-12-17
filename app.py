

"""_summary_
Books store web scrapper 
"""
import time
import logging
from tqdm import tqdm
from pages.books_page import BooksPage
from utils.utilities import fetch_page, display_ascii_art
from utils.constants import BOOKS_STORE_URL

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading books list...')

page_content = fetch_page(BOOKS_STORE_URL)
page = BooksPage(page_content)
books = page.books

for page_num in tqdm(range(1, page.page_count), 
                    desc="Processing", bar_format="{l_bar}{bar} [ time left: {remaining} ]"):
    url = f'{BOOKS_STORE_URL}/catalogue/page-{page_num+1}.html'

    page_content = fetch_page(url)

    logger.debug(f'Creating BooksPage from {url}')
    
    page = BooksPage(page_content)
    books.extend(page.books)
    time.sleep(0.1)

display_ascii_art()
