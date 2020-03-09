
# Author:Yi Sun(Tim) 2018

'''Test Login Page'''

import unittest
from Code_Sample.Login_163mail import *
from selenium import webdriver
import time as t

class MailTest(unittest.TestCase,mail):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://mail.163.com")

    def tearDown(self):
        self.driver.quit()

    def test_163Login_001(self):
        '''登录业务：账号密码为空验证'''
        self.login(",")
        self.assertEqual(self.getLoginError,'请输入邮箱名')

    def test_163Login_002(self):
        '''登录业务：输入不规范邮箱名'''
        self.login('sanjieyu','123456')
        self.assertEqual(self.getLoginError,'输入的邮箱名格式不对')

if __name__ == '__main__':
    unittest.main(verbosity=2)
