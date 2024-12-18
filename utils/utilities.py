

"""_summary_
    This uitiity module contains the fetch_page function that fetches the content of a given URL, 
    and the ASCII_ART variable that contains the ASCII art for the application.
"""

import requests
import pyfiglet
import os
import logging
from requests.exceptions import RequestException, Timeout
from utils.constants import CURRENCY_INFO, CURRENCY_CONVERTER_API_URL


logger = logging.getLogger('scraping.utilities')

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
        logger.error(f"Request to {url} timed out.")
        raise
    except RequestException as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")
        raise

def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    """Fetch the exchange rate from base_currency to target_currency."""
    api_url = f"{CURRENCY_CONVERTER_API_URL}{base_currency}"
    response = requests.get(api_url, timeout=10)
    data = response.json()
    return data['rates'][target_currency]



def convert_price(price: float, exchange_rate: float) -> float:
    """Convert the price using the given exchange rate."""
    return price * exchange_rate

def get_currency_info(currency_code):
    """Get the currency info for the given currency code."""
    return CURRENCY_INFO.get(currency_code, {'symbol': currency_code, 'country': 'Unknown'})


def display_ascii_art() -> str:
    """Display the ASCII art for the application."""
    ascii_art = pyfiglet.figlet_format("Book Scraper", font="slant")
    print(ascii_art)

def clear_console():
    """Clear the console based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def truncate_title(title: str, max_length: int = 100) -> str:
    """Truncate the title to the given length.

    Args:
        title (str): The title to truncate.
        max_length (int, optional): The maximum length of the title. Defaults to 50.

    Returns:
        str: The truncated title.
    """
    return title if len(title) <= max_length else title[:max_length - 3] + '...'