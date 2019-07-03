import unittest
from time import sleep
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class Tongcheng58(unittest.TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://passport.58.com/login/")

    def login(self,username,password):
        user_pass = self.chrome.find_element_by_class_name("qrcode")
        user_pass.click()
        username_u1 = self.chrome.find_element_by_id("username")
        password_u1 = self.chrome.find_element_by_id("password")
        button = self.chrome.find_element_by_id("btn_account")
        username_u1.send_keys(username)
        password_u1.send_keys(password)
        button.click()

        text = self.chrome.find_element_by_class_name("password_msgtext").text

        return text

    def test_login_one(self):
        text = self.login("13371054432","123")
        self.assertEqual("密码太短，最少6位",text,"密码太短，提示内容有误")

    def test_login_two(self):
        text = self.login("13371054432","123456")
        self.assertEqual("该用户不存在",text,"账户有误，提示内容有误")
    def tearDown(self):
        sleep(10)
        self.chrome.close()


if __name__ == '__main__':
    # unittest.main()
    # 使用HTMLTestRunner进行测试
    suite = unittest.TestSuite()
    suite.addTest(Tongcheng58("test_login_one"))
    suite.addTest(Tongcheng58("test_login_two"))
    with open("report.html","wb") as f:
        runner = HTMLTestRunner(
            stream=f,
            title="58登录测试",
            description="简单的账户登录自动化测试"
        )
        runner.run(suite)

