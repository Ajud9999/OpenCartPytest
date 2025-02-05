import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import os
import time


class Test_Login():
    baseURL = "https://demo.opencart.com/en-gb?route=account/login"
    logger = LogGen.loggen()

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
         self.logger.info("******* Starting test_002_login **********")
         self.driver=setup
         self.driver.get(self.baseURL)
         self.driver.maximize_window()
         time.sleep(3)

         self.lp= LoginPage(self.driver)
         self.lp.setEmail(self.user)
         self.lp.setPassword(self.password)

         # self.driver.execute_script("window.scrollBy(0,300)", "")
         time.sleep(1)

         self.lp.clickLogin()
         time.sleep(5)

         self.targetpage = self.lp.isMyAccountPageExists()
         if self.targetpage==True:
            assert True
         else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
            assert False

         self.driver.close()
         self.logger.info("******* End of test_002_login **********")
