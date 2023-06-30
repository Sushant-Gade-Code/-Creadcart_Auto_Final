from selenium import webdriver
from PageObjects.LogInPage import LogINPage
from Utility.log import LogGenerator


class Test_login_param:
    baseurl='https://automation.credence.in/'
    log=LogGenerator.loggen()
    def test_login_param__004(self,Setup,getDataForLgoIn):
        self.log.info("TestCase test_login_param__004 Started....!")
        self.driver=Setup
        self.log.info("TestCase test_login_003 Passed....!")
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.log.info("Opening The URL Is Done....!")
        self.lp2=LogINPage(self.driver)
        self.lp2.getLogInLink()
        self.log.info("Getting the getLogInLink Link Is Successfully....!")
        self.lp2.getemailAdd(getDataForLgoIn[0])
        self.log.info("Getting the Email_Name Is Successfully....!")
        self.lp2.emailpassword(getDataForLgoIn[1])
        self.log.info("Getting the Password Is Successfully....!")
        self.lp2.getLoginButton()
        self.log.info("Getting the LoginButton Is Successfully....!")
        act_title=self.driver.title
        self.log.info("Capturing The Page Title Is Successfully....!")
        exp_title="CredKart"
        if act_title==exp_title:
            self.log.info(" act_title and exp_title is Passed....!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_login_param__004Passed.png")
            if getDataForLgoIn[2]=="Pass":
                self.log.info(" getDataForLgoIn[2]=='Pass' is Passed....!")
                self.lp2.getMenuButton()
                self.log.info("Getting the MenuButton Is Successfully....!")
                self.lp2.getLogOutButton()
                self.log.info("Getting the LogOutButton Is Successfully....!")
                assert True
            else:
                self.log.info(" getDataForLgoIn[2]=='Pass' is Failed....!")
                assert False

        else:
            self.log.info(" act_title and exp_title is Failed....!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase_test_login_param__004Passed.png")
            if getDataForLgoIn[2] == "Fail":
                self.log.info(" getDataForLgoIn[2]=='Fail' is Passed....!")
                self.lp2.getMenuButton()
                self.log.info("Getting the MenuButton Is Successfully....!")
                self.lp2.getLogOutButton()
                self.log.info("Getting the LogOutButton Is Successfully....!")
                assert True
            else:
                self.log.info(" getDataForLgoIn[2]=='Fail' is Failed....!")
                assert False

        self.driver.close()









# from selenium import webdriver
# from PageObjects.LogInPage import LogINPage
# class Test_login_param:
#     baseurl='https://automation.credence.in/'
#
#     def test_login_param__001(self,Setup,getDataForLgoIn):
#         self.driver=Setup
#         self.driver.implicitly_wait(10)
#         self.driver.get(self.baseurl)
#         self.lp2=LogINPage(self.driver)
#         self.lp2.getLogInLink()
#         self.lp2.getemailAdd(getDataForLgoIn[0])
#         self.lp2.emailpassword(getDataForLgoIn[1])
#         self.lp2.getLoginButton()
#         act_title=self.driver.title
#         exp_title="CredKart"
#         if act_title==exp_title:
#             assert True
#             self.lp2.getMenuButton()
#             self.lp2.getLogOutButton()
#         else:
#             self.driver.close()
#             assert False




