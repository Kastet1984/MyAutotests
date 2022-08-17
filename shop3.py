import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
pending_approval = driver.find_element(By.CSS_SELECTOR, ".orderby >[value='menu_order']")
pending_approval_checked = pending_approval.get_attribute("selected")
assert pending_approval_checked == "true"
element = driver.find_element(By.CLASS_NAME, "orderby")
select = Select(element)
select.select_by_value("price-desc")
time.sleep(2)
element = driver.find_element(By.CLASS_NAME, "orderby")
pending_approval = driver.find_element(By.CSS_SELECTOR, ".orderby >[value='price-desc']")
pending_approval_checked = pending_approval.get_attribute("selected")
assert pending_approval_checked == "true"

