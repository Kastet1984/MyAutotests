import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account_btn = driver.find_element(By.LINK_TEXT, "My Account")
time.sleep(2)
my_account_btn.click()
time.sleep(2)
email_address = driver.find_element(By.ID, "username")
email_address.send_keys("vfrc@list.ru")
password = driver.find_element(By.ID, "password")
password.send_keys("q12we34rt56y")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
time.sleep(2)
shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
time.sleep(2)
shop_btn.click()
time.sleep(2)
html_btn = driver.find_element(By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/product-category/html/']")
time.sleep(2)
html_btn.click()
time.sleep(2)
items_count = driver.find_elements(By.CLASS_NAME, "woocommerce-LoopProduct-link")
assert len(items_count) == 3
