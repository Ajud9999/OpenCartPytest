from selenium.webdriver.common.by import By


class HomePage():
     link_myaccount_xpath = "/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[1]/li[2]/div[1]/a[1]/span[1]"
     link_register_xpath = "//a[normalize-space()='Register']"
     link_login_xpath = "//a[normalize-space()='Login']"


     def __init__(self, driver):
         self.driver=driver

     def clickMyAccount(self):
         self.driver.find_element(By.XPATH, self.link_myaccount_xpath).click()


     def clickRegister(self):
         self.driver.find_element(By.XPATH, self.link_register_xpath).click()


     def clickLogin(self):
         self.driver.find_element(By.XPATH, self.link_login_xpath).click()


         
