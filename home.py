import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
sel_ruby_book = driver.find_element_by_css_selector("[alt='Selenium Ruby']")
driver.execute_script("return arguments[0].scrollIntoView(true);", sel_ruby_book)
time.sleep(2)
sel_ruby_book.click()
time.sleep(2)
reviews = driver.find_element_by_css_selector("[href='#tab-reviews']")
reviews.click()
time.sleep(2)
stars_5 = driver.find_element_by_class_name("star-5")
stars_5.click()
comment_area = driver.find_element_by_id("comment")
comment_area.send_keys("Nice book!")
name_area = driver.find_element_by_id("author")
name_area.send_keys("Maximus")
email_area = driver.find_element_by_id("email")
email_area.send_keys("vfrc@list.ru")
submit_btn = driver.find_element_by_class_name("submit")
submit_btn.click()
