

"""_summary_
Books store web scrapper 
"""

import requests
from bs4 import BeautifulSoup

page_content = requests.get('http://books.toscrape.com').content
soup = BeautifulSoup(page_content, 'html.parser')

test_content = soup.select_one('div.page-header h1').string

print(test_content)