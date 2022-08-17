import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
time.sleep(1)
shop_btn.click()
time.sleep(1)
add_basket_btn = driver.find_element(By.CSS_SELECTOR, "[href='/shop/?add-to-cart=182']")
add_basket_btn.click()
time.sleep(1)
items = driver.find_element(By.CLASS_NAME, "cartcontents")
items_get_text = items.text
assert items_get_text == "1 Item"
price = driver.find_element(By.XPATH, "//span[text()='₹180.00']")
price_get_text = price.text
assert price_get_text == "₹180.00"
basket = driver.find_element(By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/basket/']")
time.sleep(1)
basket.click()
time.sleep(1)
subtotal_price = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal'] > span"), "₹180.00"))


total_price = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Total'] >strong >span"), "₹183.60"))

