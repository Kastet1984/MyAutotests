import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
time.sleep(1)
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
book_HTML5_btn = driver.find_element(By.CSS_SELECTOR, "[href='/shop/?add-to-cart=182']")
book_HTML5_btn.click()
time.sleep(1)
book_JS_btn = driver.find_element(By.CSS_SELECTOR, "[href='/shop/?add-to-cart=180']")
book_JS_btn.click()
basket = driver.find_element(By.CSS_SELECTOR, "[title='View Basket']")
time.sleep(3)
basket.click()
time.sleep(3)
del_book_HTML5_btn = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
del_book_HTML5_btn.click()
time.sleep(1)
undo_btn = driver.find_element(By.LINK_TEXT, "Undo?")
undo_btn.click()
quantity = driver.find_element(By.NAME, "cart[4c5bde74a8f110656874902f07378009][qty]")
quantity.clear()
quantity = driver.find_element(By.NAME, "cart[4c5bde74a8f110656874902f07378009][qty]")
quantity.send_keys("3")
up_basket_btn = driver.find_element(By.NAME, "update_cart")
time.sleep(1)
up_basket_btn.click()
time.sleep(1)
items = driver.find_element(By.NAME, "cart[4c5bde74a8f110656874902f07378009][qty]")
items_check = items.get_attribute("value")
assert items_check == "3"
time.sleep(1)
apply_coupon_btn = driver.find_element(By.NAME, "apply_coupon")
apply_coupon_btn.click()
items = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error > li")
items_check = items.text
assert items_check == "Please enter a coupon code."


