from bs4 import BeautifulSoup
from utils.ocado import scrape_product
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

url = 'https://www.ocado.com/browse'

driver.get(url)
html = driver.page_source

sl_items = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'fops-item fops-item--on_offer')))

browse_page = BeautifulSoup(html, 'html.parser')

with open('selenium_html.html', 'w') as file:
    file.write(browse_page.prettify())

items = browse_page.find_all('li', class_ ='fops-item fops-item--on_offer')

for item in items:
    print(scrape_product(item))