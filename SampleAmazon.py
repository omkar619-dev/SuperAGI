from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initializing the WebDriver
driver = webdriver.Chrome()

# Opening up Amazon.in
driver.get('https://www.amazon.in')

# Waiting for the page to load
time.sleep(5)

#Search for 'lg soundbar'
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys('lg soundbar')
search_box.send_keys(Keys.RETURN)

time.sleep(5)

#Reading the product names and associated main prices on the search result page
products = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")

#Putting the product names and prices in a key-value pair dictionary
product_price_dict = {}

for product, price in zip(products, prices):
    product_name = product.text
    product_price = price.text.replace(',', '') if price.text else '0'
    product_price_dict[product_name] = int(product_price)

#Handling cases where price is missing, assigning them to 0.
for product in products[len(prices):]:
    product_name = product.text
    product_price_dict[product_name] = 0

# Sorting by price
sorted_products = sorted(product_price_dict.items(), key=lambda x: x[1])

# Outputting the results correctly (product price first, then product name)
for product, price in sorted_products:
    print(f"{price} {product}")

# Closing the browser
driver.quit()
