import time
import os

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestAccountRegistration():
    # baseURL = "https://demo.opencart.com/"
    # baseURL = ReadConfig.getApplicationURL()
    baseURL = "https://demo.opencart.com/en-gb?route=account/register"
    logger = LogGen.loggen()  # for logging

    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.logger.info("**** test_001_AccountRegistration started *** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)

        # Initialize page objects
        # self.hp = HomePage(self.driver)
        # self.hp.clickMyAccount()
        # time.sleep(10)
        # self.hp.clickRegister()
        # time.sleep(10)

        self.logger.info("Proving customer details for registration")
        self.repage = AccountRegistrationPage(self.driver)
        self.repage.setFirstName("Ajit")
        self.repage.setLastName("Devkar")

        # Generate a random email
        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.repage.setEmail(self.email)
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)

        self.repage.setPassword("abcxyz")
        self.repage.setPrivacyPolicy()
        self.repage.clickContinue()
        time.sleep(5)

        self.confmsg = self.repage.getConfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account registration is passed..")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
            self.logger.error("Account registration is failed.")
            self.driver.close()
            assert False

        self.logger.info("**** test_001_AccountRegistration Finished *** ")
