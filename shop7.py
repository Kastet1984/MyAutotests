import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
time.sleep(1)
shop_btn.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
book_HTML5_btn = driver.find_element(By.CSS_SELECTOR, "[href='/shop/?add-to-cart=182']")
book_HTML5_btn.click()
basket = driver.find_element(By.CSS_SELECTOR, "[title='View Basket']")
basket.click()
checkout_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.alt.wc-forward")))
checkout_btn.click()
time.sleep(1)
first_name_field = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name_field.send_keys("Maxim")
last_name_field = driver.find_element(By.ID, "billing_last_name")
last_name_field.send_keys("Yarochkin")
email_field = driver.find_element(By.ID, "billing_email")
email_field.send_keys("vfrc84@list.ru")
phone_field = driver.find_element(By.ID, "billing_phone")
phone_field.send_keys("+79110373477")
country_field = driver.find_element(By.ID, "select2-chosen-1")
country_field.click()
country = driver.find_element(By.ID, "s2id_autogen1_search")
country.send_keys("Russia")
time.sleep(1)
country_choice = driver.find_element(By.ID, "select2-results-1")
country_choice.click()
street_field = driver.find_element(By.NAME, "billing_address_1")
street_field.send_keys("Nevsky")
apart_field = driver.find_element(By.NAME, "billing_address_2")
apart_field.send_keys("100")
town_field = driver.find_element(By.NAME, "billing_city")
town_field.send_keys("Piter")
state_field = driver.find_element(By.NAME, "billing_state")
state_field.send_keys("Piter")
postcode_field = driver.find_element(By.NAME, "billing_postcode")
postcode_field.send_keys("198300")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payment_btn = driver.find_element(By.ID, "payment_method_cheque")
check_payment_btn.click()
place_order_btn = driver.find_element(By.ID, "place_order")
place_order_btn.click()

