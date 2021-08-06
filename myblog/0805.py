from selenium import webdriver
import time

import unittest
from ddt import ddt


@ddt
class myblog(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:8080/myblog_war_exploded/login.html"
        self.driver.maximize_window()
        time.sleep(3)


    def tearDown(self):
        self.driver.close()


    def testLogin(self):
        driver = self.driver
        driver.find_element_by_id("username").send_keys("18220111862")
        driver.find_element_by_name("password").send_keys("sq000...")

    if __name__ == "__main__":
        unittest.main()
