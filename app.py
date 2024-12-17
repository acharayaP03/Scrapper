

"""_summary_
Books store web scrapper 
"""
import time
import requests
from tqdm import tqdm
import pyfiglet
from colorama import init, Fore, Style
from pages.books_page import BooksPage
from requests.exceptions import RequestException, Timeout

init()

ASCII_ART = pyfiglet.figlet_format(f"Book Scraper", font="slant")

def fetch_page(url: str) -> bytes:
    """Fetch the content of the given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        bytes: The content of the response.

    Raises:
        RequestException: If there is an issue with the request.
        Timeout: If the request times out.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.content
    except Timeout:
        print(f"Request to {url} timed out.")
        raise
    except RequestException as e:
        print(f"An error occurred: {e}")
        raise


page_content = fetch_page('http://books.toscrape.com')
page = BooksPage(page_content)
books = page.books

# Print ASCII art
print(ASCII_ART)


for page_num in tqdm(range(1, page.page_count), desc="Processing", bar_format="{l_bar}{bar} [ time left: {remaining} ]"):
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = fetch_page(url)
    page = BooksPage(page_content)
    books.extend(page.books)
    time.sleep(0.1)