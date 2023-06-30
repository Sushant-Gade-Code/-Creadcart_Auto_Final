import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Utility.ReadProperties import ReadProperties
from PageObjects.RegistrationPage import Registration
from Utility.log import LogGenerator


class Test_registration:
    url=ReadProperties.getBaseUrl()
    name=ReadProperties.geteNameR()
    email=ReadProperties.getemailR()
    passw=ReadProperties.getepasswordR()
    conpassw=ReadProperties.geteconfirmPassR()
    log = LogGenerator.loggen()
    def test_HomePageTitle__001(self,Setup):
        self.log.info("TestCase test_HomePageTitle__001 Started....!")
        self.driver=Setup
        self.log.info("Initializing webdriver Is Done....!")
        self.driver.get(self.url)
        self.log.info("Opening The URL Is Done....!")
        act_Title=self.driver.title
        self.log.info("Capturing The Page Title Is Done....!")
        exP_Title="CredKart"
        if act_Title==exP_Title:
            self.log.info("test_HomePageTitle__001 Passed....!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_HomePageTitle__001_Passed.png")
            assert True
            self.driver.close()
        else:
            self.log.info("test_HomePageTitle__001 Failed....!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_HomePageTitle__001_Failed.png")
            self.driver.close()
            assert False

    def test_Registration__002(self,Setup):
        self.log.info("TestCase test_Registration__002 Started....!")
        self.driver=Setup
        self.log.info("Initializing webdriver Is Done....!")
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.log.info("Opening The URL Is Done....!")
        self.lp=Registration(self.driver)
        self.lp.getegistrationlink()
        self.log.info("Getting the Resgistration Link Is Successfully....!")
        self.lp.getReg_Name(self.name)
        self.log.info("Getting the Name Is Successfully....!")
        self.lp.getEmaliadd(self.email)
        self.log.info("Getting the Email_Name Is Successfully....!")
        self.lp.getPassword(self.passw)
        self.log.info("Getting the Password Is Successfully....!")
        self.lp.getConfPassword(self.conpassw)
        self.log.info("Getting the Confirmed Password Is Successfully....!")
        self.lp.getRegistrationButton()
        self.log.info("Getting the RegistrationButton Is Successfully....!")
        time.sleep(3)
        act_Title = self.driver.find_element(By.XPATH,'//a[text()="Blog Post"]').text
        self.log.info("Capturing The Page Title Is Successfully....!")
        print(act_Title)
        exP_Title = "Blog Post"
        if act_Title == exP_Title:
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_Registration__002Passed.png")
            self.log.info("TestCase test_Registration__002 Passed....!")
            assert True
            self.driver.close()
        else:
            self.log.info("TestCase test_Registration__002 Failed....!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_Registration__002Failed.png")
            self.driver.close()
            assert False

