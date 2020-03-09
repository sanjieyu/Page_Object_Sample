
# Author:Yi Sun(Tim) 2018

'''test weibo page'''

import unittest
import time as t

from appium import webdriver
from Code_Sample.weibo import WeiBo

class WeiBoTest(unittest.TestCase,WeiBo):
    def setUp(self):
        desired.caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'meizu_M5'
        desired_caps['appPackage'] = 'com.sina.weibo'
        desired_caps['appActivity'] = 'com.sina.weibo.SplashActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def test_001(self):
        t.sleep(3)
        self.getPhoneCode('18651669226')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
