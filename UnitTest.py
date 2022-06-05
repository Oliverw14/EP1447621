from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox()
driver.get("https://oliverw14.pythonanywhere.com/register")
elem = driver.find_element_by_name("username")
elem.send_keys('Oliverw14')
elem = driver.find_element_by_name("firstname")
elem.send_keys('Oliver')
elem = driver.find_element_by_name("lastname")
elem.send_keys('Wilson')
elem = driver.find_element_by_name("email_address")
elem.send_keys('UnitTest@test.com')
elem = driver.find_element_by_name("password_1")
elem.send_keys('password123')
elem = driver.find_element_by_name("password_2")
elem.send_keys('password123')
elem.send_keys(Keys.ENTER)
assert "No results found." not in driver.page_source
driver.close()