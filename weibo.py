
# Author:Yi Sun(Tim) 2018

'''weibo page'''


from Code_Sample.basePage import *
import time as t

class WeiBo(AppUI):
    login_loc = (By.ID,'login')
    phone_loc = (By.ID,'input phone number')
    codeButton_loc = (By.ID,'get code')

    @property
    def clickMy(self):
        t.sleep(3)
        self.findElement(*self.login_loc).click()

    def typePhone(self,phone):
        self.findElement(*self.phone_loc).send_keys(phone)

    def clickCodeButton(self):
        self.findElement(*self.codeButton_loc).click()

    def getPhoneCode(self,phone):
        self.clickMy
        self.typePhone()
        self.clickCodeButton()
