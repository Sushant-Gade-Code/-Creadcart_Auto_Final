from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LogInPage import LogINPage
from Utility.log import LogGenerator


class Test_loginPage:
    baseUrl="https://automation.credence.in/"
    email="svgade2122@gmail.com"
    password='sushant'
    log=LogGenerator.loggen()
    def test_login_003(self,Setup):
        self.log.info("TestCase test_login_003 Started....!")
        self.driver=Setup
        self.log.info("TestCase test_login_003 Passed....!")
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)
        self.log.info("Opening The URL Is Done....!")
        self.lp1=LogINPage(self.driver)
        self.lp1.getLogInLink()
        self.log.info("Getting the getLogInLink Link Is Successfully....!")
        self.lp1.getemailAdd(self.email)
        self.log.info("Getting the Email_Name Is Successfully....!")
        self.lp1.emailpassword(self.password)
        self.log.info("Getting the Password Is Successfully....!")
        self.lp1.getLoginButton()
        self.log.info("Getting the LoginButton Is Successfully....!")
        act_Title = self.driver.find_element(By.XPATH, '//a[text()="Blog Post"]').text
        self.log.info("Capturing The Page Title Is Successfully....!")
        exP_Title = "Blog Post"
        if act_Title == exP_Title:
            self.log.info("TestCase test_login_003 Passed....!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_login_003Pass.png")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_login_003Fail.png")
            self.log.info("TestCase test_login_003 Failed....!")
            self.driver.close()
            assert False
