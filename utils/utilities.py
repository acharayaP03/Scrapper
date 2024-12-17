

"""_summary_
    This uitiity module contains the fetch_page function that fetches the content of a given URL, 
    and the ASCII_ART variable that contains the ASCII art for the application.
"""

import requests
import pyfiglet
import os
from requests.exceptions import RequestException, Timeout


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

def display_ascii_art():
    """Display the ASCII art for the application."""
    ASCII_ART = pyfiglet.figlet_format(f"Book Scraper", font="slant")
    print(ASCII_ART)

def clear_console():
    """Clear the console based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')