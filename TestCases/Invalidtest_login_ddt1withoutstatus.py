from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LogInPage import LogINPage
from Utility.ExcelUtility import Xlutil

import time
class Test_loginPage:
    baseUrl="https://automation.credence.in/"
    File ="C:\\Users\\Admin\\PycharmProjects\\CreadCart_Auto_final\\TestData\\loginecel1.xlsx"
    def test_login_003(self,Setup):
        self.driver=Setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)
        self.lp1=LogINPage(self.driver)


        self.rows=Xlutil.getRowCount(self.File,'Sheet1')
        print(self.rows)
        aList=[]
        for r in range(2,6):
            self.email=Xlutil.getReadData(self.File,"Sheet1",r,1)
            self.password=Xlutil.getReadData(self.File,"Sheet1",r,2)
            self.Exp_result=Xlutil.getReadData(self.File,"Sheet1",r,3)
            time.sleep(2)
            self.lp1.getLogInLink()
            time.sleep(5)
            self.lp1.getemailAdd(self.email)
            time.sleep(2)
            self.lp1.emailpassword(self.password)
            time.sleep(2)
            self.lp1.getLoginButton()
            time.sleep(2)
            act_Title = self.driver.find_element(By.XPATH,'//div[@class="jumbotron text-center clearfix"]/h2').text
            print(act_Title)
            exP_Title = "CredKart"
            if  act_Title== exP_Title:
                if  self.Exp_result=="Pass":
                    self.lp1.getMenuButton()
                    time.sleep(1)
                    self.lp1.getLogOutButton()
                    time.sleep(2)
                    aList.append("Pass")
                elif self.Exp_result=="Fail":
                    self.lp1.getMenuButton()
                    time.sleep(2)
                    try:
                        self.lp1.getLogOutButton()
                    except:
                        None
                    time.sleep(1)
                    aList.append("Fail")
            elif act_Title== exP_Title:
                if self.Exp_result=="Pass":
                    aList.append("Fail")
                elif self.Exp_result=="Fail":
                    aList.append("Pass ")
        print(aList)
        if "Fail" not in aList:
            self.driver.close()
            assert True
        else:
            assert False









