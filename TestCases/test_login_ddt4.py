from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LogInPage import LogINPage
from Utility.ExcelUtility import Xlutil

import time

from Utility.log import LogGenerator


class Test_loginPage:
    baseUrl="https://automation.credence.in/"
    File ="C:\\Users\\Admin\\PycharmProjects\\CreadCart_Auto_final\\TestData\\loginecel1.xlsx"
    log = LogGenerator.loggen()
    def test_login_005(self,Setup):
        self.log.info("TestCase test_login_005 Started....!")
        self.driver=Setup
        self.log.info("Initializing webdriver Is Done....!")
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)
        self.log.info("Opening The URL Is Done....!")
        self.lp1=LogINPage(self.driver)
        self.rows=Xlutil.getRowCount(self.File,'Sheet1')
        print(self.rows)
        aList=[]
        for r in range(2,6):
            self.email=Xlutil.getReadData(self.File,"Sheet1",r,1)
            self.password=Xlutil.getReadData(self.File,"Sheet1",r,2)
            self.Exp_result=Xlutil.getReadData(self.File,"Sheet1",r,3)
            time.sleep(5)
            self.lp1.getLogInLink()
            self.log.info("Getting the getLogInLink Link Is Successfully....!")
            time.sleep(5)
            self.lp1.getemailAdd(self.email)
            self.log.info("Getting the Email_Name Is Successfully....!")
            time.sleep(5)
            self.lp1.emailpassword(self.password)
            self.log.info("Getting the Password Is Successfully....!")
            time.sleep(5)
            self.lp1.getLoginButton()
            self.log.info("Getting the LoginButton Is Successfully....!")
            time.sleep(5)
            act_Title = self.driver.title
            self.log.info('Capturing The Page Title Is Successfully....>"{self.act_Title}"!')
            print(act_Title)
            exP_Title = "CredKart"
            if  self.lp1.Status() == True:
                if  self.Exp_result=="Pass":
                    self.lp1.getMenuButton()
                    self.log.info("Click on Menu button")
                    time.sleep(3)
                    self.lp1.getLogOutButton()
                    self.log.info("Getting the LogOutButton Is Successfully....!")
                    time.sleep(3)
                    aList.append("Pass")
                elif self.Exp_result=="Fail":
                    self.lp1.getMenuButton()
                    self.log.info("Click on Menu button")
                    time.sleep(3)
                    self.lp1.getLogOutButton()
                    self.log.info("Getting the LogOutButton Is Successfully....!")
                    time.sleep(3)
                    aList.append("Fail")
            elif self.lp1.Status() == False:
                if self.Exp_result=="Pass":
                    aList.append("Fail")
                elif self.Exp_result=="Fail":
                    aList.append("Pass ")

        print(aList)
        if "Fail" not in aList:
            self.log.info("TestCase test_login_005 Passed")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_login_005Pass.png")
            self.driver.close()
            assert True
        else:
            self.log.info("TestCase test_login_005 Failed")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_login_005Fail.png")
            assert False









