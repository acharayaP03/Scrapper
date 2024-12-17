

"""_summary_
Books store web scrapper 
"""
import time
import logging
from tqdm import tqdm
from pages.books_page import BooksPage
from utils.utilities import fetch_page, display_ascii_art

BOOKS_STORE_URL = 'http://books.toscrape.com'

page_content = fetch_page(BOOKS_STORE_URL)
page = BooksPage(page_content)
books = page.books

for page_num in tqdm(range(1, page.page_count), 
                    desc="Processing", bar_format="{l_bar}{bar} [ time left: {remaining} ]"):
    
    url = f'{BOOKS_STORE_URL}/catalogue/page-{page_num+1}.html'

    page_content = fetch_page(url)
    
    page = BooksPage(page_content)
    books.extend(page.books)
    time.sleep(0.1)

display_ascii_art()
