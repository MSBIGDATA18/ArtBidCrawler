from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

path = '/Users/mawensalignat-moandal/Desktop/Selenium/chromedriver-mac-arm64/chromedriver'
web = 'https://www.gros-delettrez.com/catalogue/155234-arts-decoratifs-du-xxe?saleSlug=arts-decoratifs-du-xxe&'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(web)
time.sleep(5)  # Adding a sleep to allow the page to load properly

# Find all product elements
products_arts = driver.find_elements(By.XPATH, '//div[contains(@class, "ordre_false product clearfix vente155234 venteEtude1 venteEtude2")]')

for product in products_arts:
    try:
        product_title = product.find_element(By.XPATH, './/div[contains(@class, "product-title")]').text
        product_description = product.find_element(By.XPATH, './/div[contains(@class, "product-description")]').text
        product_flash = product.find_element(By.XPATH, './/div[contains(@class, "sale-flash2")]').text

        print(f"Title: {product_title}")
        print(f"Description: {product_description}")
        print(f"Flash: {product_flash}")
    except Exception as e:
        print(f"Error processing product: {e}")

time.sleep(10)
driver.quit()



