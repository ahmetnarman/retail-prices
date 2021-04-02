from bs4 import BeautifulSoup
import requests


def scrape_item(item):
    name_item = item.find('h4', class_ = "fop-title")
    if name_item:
        return name_item.text
    return None

url = 'https://www.ocado.com/browse'

html_text = requests.get(url).text
browse_page = BeautifulSoup(html_text, 'lxml')

items = browse_page.find_all('li', class_ ='fops-item fops-item--on_offer')

for item in items:
    print(scrape_item(item))

