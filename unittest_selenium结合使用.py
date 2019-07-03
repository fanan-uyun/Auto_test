import unittest
from time import sleep
from selenium import webdriver

class Tongcheng58(unittest.TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://passport.58.com/login/")

    def test_login_one(self):
        user_pass = self.chrome.find_element_by_class_name("qrcode")
        user_pass.click()
        username_u1 = self.chrome.find_element_by_id("username")
        password_u1 = self.chrome.find_element_by_id("password")
        button = self.chrome.find_element_by_id("btn_account")

        username_u1.send_keys("13371054432")
        password_u1.send_keys("123")
        button.click()

        text = self.chrome.find_element_by_class_name("password_msgtext").text

        self.assertEqual("密码太短，最少6位",text,"密码太短，提示内容有误")

    def test_login_two(self):
        user_pass = self.chrome.find_element_by_class_name("qrcode")
        user_pass.click()
        username_u1 = self.chrome.find_element_by_id("username")
        password_u1 = self.chrome.find_element_by_id("password")
        button = self.chrome.find_element_by_id("btn_account")

        username_u1.send_keys("13371054432")
        password_u1.send_keys("1234567")
        button.click()

        text = self.chrome.find_element_by_class_name("password_msgtext").text

        self.assertEqual("该用户名与密码不符",text,"密码错误，提示内容有误")
    def tearDown(self):
        sleep(10)
        self.chrome.close()


if __name__ == '__main__':
    unittest.main()

