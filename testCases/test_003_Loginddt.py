import time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login_DDT():
    # baseURL = ReadConfig.getApplicationURL()
    baseURL = "https://demo.opencart.com/en-gb?route=account/login"
    logger = LogGen.loggen()  # Logger

    path = os.path.abspath(os.curdir)+"\\testData\\Opencart_LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)


        self.lp = LoginPage(self.driver)  # LoginPage Page Object Class
        self.ma = MyAccountPage(self.driver)  # MyAccount Page Object class
        # self.driver.execute_script("window.scrollBy(0,200)", "")

        for r in range(2,self.rows+1):

            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.clearEmail()
            time.sleep(1)
            self.lp.setEmail(self.email)
            time.sleep(2)
            self.lp.clearPassword()
            time.sleep(1)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.clickLogin()
            time.sleep(3)
            # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            # time.sleep(3)
            self.targetpage=self.lp.isMyAccountPageExists()

            # if self.exp=='Valid':
            #     if self.targetpage==True:
            #         lst_status.append('Pass')
            #         self.ma.clickLogout()
            #         time.sleep(5)
            #     else:
            #         lst_status.append('Fail')
            # elif self.exp=='Invalid':
            #     if self.targetpage == True:
            #         lst_status.append('Fail')
            #         self.ma.clickLogout()
            #         time.sleep(5)
            #     else:
            #         lst_status.append('Pass')

            if self.exp=='Invalid':
                if self.targetpage==True:
                    lst_status.append('Fail')
                    # self.ma.clickLogout()
                    time.sleep(2)
                else:
                    lst_status.append('Pass')
            elif self.exp=='Valid':
                if self.targetpage == True:
                    lst_status.append('Pass')
                    # self.ma.clickLogout()
                    time.sleep(2)
                else:
                    lst_status.append('Fail')

        self.driver.close()

        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")
