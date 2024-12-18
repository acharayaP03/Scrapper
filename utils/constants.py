"""_summary_
This module contains the constants used in the application.
"""
from colorama import init, Fore, Style

init()

USER_CHOICE = f"""{Fore.GREEN}Enter one of the following

- 'b' to look at the best books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to quit

Enter your choice: {Style.RESET_ALL}"""

BOOKS_STORE_URL = 'http://books.toscrape.com'

CURRENCY_CONVERTER_API_URL = 'https://api.exchangerate-api.com/v4/latest/'

CURRENCY_INFO = {
    'USD': {'symbol': '$', 'country': 'United States'},
    'EUR': {'symbol': '€', 'country': 'Eurozone'},
    'GBP': {'symbol': '£', 'country': 'United Kingdom'},
    'JPY': {'symbol': '¥', 'country': 'Japan'},
    'AUD': {'symbol': 'A$', 'country': 'Australia'},
    'CAD': {'symbol': 'C$', 'country': 'Canada'},
    'CHF': {'symbol': 'CHF', 'country': 'Switzerland'},
    'CNY': {'symbol': '¥', 'country': 'China'},
    'SEK': {'symbol': 'kr', 'country': 'Sweden'},
    'NZD': {'symbol': 'NZ$', 'country': 'New Zealand'},
    'INR': {'symbol': '₹', 'country': 'India'},
    'NPR': {'symbol': '₨', 'country': 'Nepal'},
    'MXN': {'symbol': '$', 'country': 'Mexico'},
    'SGD': {'symbol': 'S$', 'country': 'Singapore'},
    'HKD': {'symbol': 'HK$', 'country': 'Hong Kong'},
    'NOK': {'symbol': 'kr', 'country': 'Norway'},
    'KRW': {'symbol': '₩', 'country': 'South Korea'},
    'TRY': {'symbol': '₺', 'country': 'Turkey'},
    'RUB': {'symbol': '₽', 'country': 'Russia'},
    'BRL': {'symbol': 'R$', 'country': 'Brazil'},
    'ZAR': {'symbol': 'R', 'country': 'South Africa'},
}
