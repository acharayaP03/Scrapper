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
