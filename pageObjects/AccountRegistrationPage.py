from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_xpath = "//input[@id='input-firstname']"
    txt_lastname_xpath = "//input[@id='input-lastname']"
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    chk_privacy_xpath = "//input[@name='agree']"
    btn_cont_xpath = "//button[normalize-space()='Continue']"
    txt_conf_msg_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"


    def __init__(self,driver):
        self.driver=driver

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.XPATH,self.chk_privacy_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()

    def getConfirmationmsg(self):
        try:
           return self.driver.find_element(By.XPATH, self.txt_conf_msg_xpath).text
        except:
           None

