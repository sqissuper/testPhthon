from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://localhost:8080/myblog_war_exploded/login.html")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("18220111862")
driver.find_element_by_name("password").send_keys("sq000...")
driver.find_element_by_id("login").click()
alert = driver.switch_to.window()
print(alert)
time.sleep(3)
driver.close()
