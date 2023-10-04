
# Author:Yi Sun(Tim) 2018

'''Login Page'''

from Code_Sample.basePage import *
from selenium.webdriver.common.by import By

class mail(WebDriver):
    username_loc = (By.ID,'username')
    password_loc = (By.ID,'password')
    login_loc = (By.LINK_TEXT,'login')
    loginError_loc = (By.XPATH,'xxxxxxx')

    def typeUserName(self,username):
        self.findElement(*self.username_loc).send_keys(username)

    def typePassword(self,password):
        self.findElement(*self.password_loc).send_keys(password)

    @property
    def clickLogin(self):
        self.findElement(*self.login_loc).click()

    def login(self,username,password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickLogin

    @property
    def getLoginError(self):
        '''获取错误的信息'''
        return self.findElement(*self.loginError_loc).text
