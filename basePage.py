

# Author:Yi Sun(Tim) 2018

'''Page Object:Base Page'''

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

class Factory(object):
    def __init__(self,driver):
        self.driver = driver

    # 工厂方法
    def createDriver(self,driver):
        if driver == 'web':
            return WebUI(self.driver)
        elif driver == 'app':
            return AppUI(self.driver)

class WebDriver(object):
    def __init__(self,driver):
        self.driver = driver

    def findElement(self,*loc):
        '''单个元素定位'''
        try:
           # return self.driver.find_element(*loc)
           return WebDriverWait(self.driver,20).until(lambda x:x.find_element(*loc))
        except NoSuchElementException as e:
            print('Error Details{0}'.format(e.args[0]))

class WebUI(WebDriver):
    def __str__(self):
        return 'WebUI'

class AppUI(WebDriver):
    def __str__(self):
        return 'AppUI'

