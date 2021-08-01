from selenium import webdriver
import time

drive = webdriver.Chrome()
drive.get("http://39.105.111.75:8081/login.html")
drive.maximize_window()

drive.find_element_by_id("username").send_keys("admin")
drive.find_element_by_id("password").send_keys("123")

drive.find_element_by_id("submit").click()
