from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LogInPage import LogINPage

from Utility.ExcelUtility import Xlutil

import time

from Utility.log import LogGenerator


class Test_loginPage_Cx_Oracle:
    baseUrl="https://automation.credence.in/"
    log = LogGenerator.loggen()

    def test_loginPage_Cx_Oracle_006(self,Setup):
        self.log.info("TestCase test_loginPage_Cx_Oracle_006 Started....!")
        self.driver=Setup
        self.log.info("Initializing webdriver Is Done....!")
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)
        self.log.info("Opening The URL Is Done....!")
        self.lp1=LogINPage(self.driver)
        import cx_Oracle
        cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_10")
        con = cx_Oracle.connect('hr/hr@localhost')
        print("connected")
        cur = con.cursor()
        s1='select * from LOGINDATA'
        cur.execute('select * from LOGINDATA')
        aList = []
        for i in cur:
            # print(i[0], "  ", i[1], "  ", i[2], "  ", i[3], "  ", i[4], "  ", i[5])
            self.lp1.getLogInLink()
            self.log.info("Getting the getLogInLink Link Is Successfully....!")
            time.sleep(5)
            self.lp1.getemailAdd(i[0])
            self.log.info("Getting the Email_Name Is Successfully....!")
            time.sleep(5)
            self.lp1.emailpassword(i[1])
            self.log.info("Getting the Password Is Successfully....!")
            time.sleep(5)
            self.lp1.getLoginButton()
            self.log.info("Getting the LoginButton Is Successfully....!")
            time.sleep(5)
            act_Title = self.driver.title
            self.log.info('Capturing The Page Title Is Successfully....>"{self.act_Title}"!')
            print(act_Title)
            exP_Title = "CredKart"
            if self.lp1.Status() == True:
                if i[2] == "Pass":
                    self.lp1.getMenuButton()
                    self.log.info("Click on Menu button")
                    time.sleep(3)
                    self.lp1.getLogOutButton()
                    self.log.info("Getting the LogOutButton Is Successfully....!")
                    time.sleep(3)
                    aList.append("Pass")
                elif i[2] =="Fail":
                    self.lp1.getMenuButton()
                    self.log.info("Click on Menu button")
                    time.sleep(3)
                    self.lp1.getLogOutButton()
                    self.log.info("Getting the LogOutButton Is Successfully....!")
                    time.sleep(3)
                    aList.append("Fail")
            elif self.lp1.Status() == False:
                if i[2] == "Pass":
                    aList.append("Fail")
                elif i[2] == "Fail":
                    aList.append("Pass")
        print(aList)
        if "Fail" not in aList:
            self.log.info("TestCase TestCase test_loginPage_Cx_Oracle_006 Passed")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_loginPage_Cx_Oracle_006Pass.png")
            self.driver.close()
            assert True
        else:
            self.log.info("TestCase TestCase test_loginPage_Cx_Oracle_006 Failed")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_loginPage_Cx_Oracle_006Fail.png")
            assert False

        cur.close()
        # con.commit()
        con.close()







