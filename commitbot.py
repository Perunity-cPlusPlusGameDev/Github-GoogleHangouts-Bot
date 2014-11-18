from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, getpass

username = raw_input("Enter yout hangout username: ")
password = getpass.getpass("Enter your hangout password: ")
driver = webdriver.Firefox()
driver.get("https://plus.google.com/hangouts")
#Sign in button
element = driver.find_element_by_id("gb_70")
element.send_keys(Keys.RETURN)
#Email
element = driver.find_element_by_id("Email")
element.send_keys(username)
#Password
element = driver.find_element_by_id("Passwd")
element.send_keys(password)
element.send_keys(Keys.RETURN)
time.sleep(5)
#this part doesn'twork
driver.find_element_by_class_name("Bb f0 ko Bm b3KmC XP").click()
driver.close()
