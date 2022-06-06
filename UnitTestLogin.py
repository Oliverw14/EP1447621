from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox()
driver.get("https://oliverw14.pythonanywhere.com/login")
elem = driver.find_element_by_name("username")
elem.send_keys('Oliverw14')
elem = driver.find_element_by_name("password")
elem.send_keys('password123')
elem.send_keys(Keys.ENTER)
assert "No results found." not in driver.page_source