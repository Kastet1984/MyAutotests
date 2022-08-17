import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account_btn = driver.find_element(By.LINK_TEXT, "My Account")
my_account_btn.click()
#email_address = driver.find_element(By.ID, "reg_email")
#email_address.send_keys("vfrc@list.ru")
#password = driver.find_element(By.ID, "reg_password")
#password.send_keys("q12we34rt56y")
#register_btn = driver.find_element(By.NAME, "register")
#register_btn.click()

email_address = driver.find_element(By.ID, "username")
email_address.send_keys("vfrc@list.ru")
password = driver.find_element(By.ID, "password")
password.send_keys("q12we34rt56y")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
logout_btn = driver.find_element(By.LINK_TEXT, "Logout")
logout_btn.click()
