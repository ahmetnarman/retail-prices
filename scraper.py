from bs4 import BeautifulSoup
from utils.ocado import scrape_product
import requests


url = 'https://www.ocado.com/browse'

html_text = requests.get(url).text

browse_page = BeautifulSoup(html_text, 'html.parser')

with open('selenium_html.html', 'w') as file:
    file.write(browse_page.prettify())

items = browse_page.find_all('li', class_ ='fops-item fops-item--on_offer')

for item in items:
    print(scrape_product(item))

