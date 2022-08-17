import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account_btn = driver.find_element(By.LINK_TEXT, "My Account")
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
html5forms_book = driver.find_element_by_css_selector(
    ".products.masonry-done > li:nth-child(3) > .woocommerce-LoopProduct-link")
html5forms_book.click()
title_element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms"))
