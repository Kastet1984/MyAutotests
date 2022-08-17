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
android_book = driver.find_element(By.CSS_SELECTOR,
                                   "[href='https://practice.automationtesting.in/product/android-quick-start-guide/']")
time.sleep(2)
android_book.click()
time.sleep(2)
old_price = driver.find_element(By.XPATH, " //span[text()='600.00']")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"
new_price = driver.find_element(By.XPATH, " //span[text()='450.00']")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"
post_image = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "attachment-shop_single.size-shop_single.wp-post-image")))
post_image.click()
post_image_close_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
post_image_close_btn.click()
