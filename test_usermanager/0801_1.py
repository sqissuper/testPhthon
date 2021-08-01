from selenium import webdriver
import time
import unittest
class userManagerTest(unittest.TestCase):

    def setUp(self):
        self.drive = webdriver.Chrome()
        self.drive.get("http://39.105.111.75:8081/login.html")
        self.drive.maximize_window()

    def tearDown(self):
        self.drive.quit()


    #登录模块
    def test_login(self):
        drive = self.drive
        drive.find_element_by_id("username").send_keys("admin")
        drive.find_element_by_id("password").send_keys("123")
        drive.find_element_by_id("submit").click()
        time.sleep(3)
        alert = drive.switch_to.alert
        alert.accept()
        time.sleep(3)




    #注册模块
    def test_regin(self):
        drive = self.drive
        drive.find_element_by_id("submit1").click()
        time.sleep(6)

        drive.find_element_by_id("username").send_keys("testBySelenium")
        drive.find_element_by_id("name").send_keys("自动化测试")
        drive.find_element_by_id("password").send_keys("123")
        drive.find_element_by_id("password2").send_keys("123")
        drive.find_element_by_id("man").click()
        drive.find_element_by_id("age").send_keys("24")
        drive.find_element_by_id("address").send_keys("西安")
        drive.find_element_by_id("qq").send_keys("111111")
        drive.find_element_by_id("email").send_keys("111111@163.com")
        drive.find_element_by_id("admin_no").click()

        drive.find_element_by_id("btn_sub").click()

        time.sleep(6)
    #主函数
    if __name__=="__main__":
        unittest.main()