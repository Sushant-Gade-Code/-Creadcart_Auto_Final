from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LogINPage:
    link_LogINButton_XPATH = (By.XPATH, '//a[text()="Login"]')
    text_Email_add_XPATH = (By.XPATH, '//input[@id="email"]')
    text_Password_XPATH = (By.XPATH, '//input[@id="password"]')
    check_Remember_XPATH = (By.XPATH, '//input[@type="checkbox"]')
    btn_LogINButton_XPATH = (By.XPATH, '//button[@type="submit"]')
    forgot_pass_XPATH = (By.XPATH, '//a[@class="btn btn-link"]')
    Button_Menu_XPATH=(By.XPATH,'//ul[@class="nav navbar-nav navbar-right"]/li[3]/a')
    Button_LogOut_XPATH=(By.XPATH,'//ul[@class="nav navbar-nav navbar-right"]/li[3]/ul/li')
    Status_text_XPATH=(By.XPATH,'//h2[normalize-space()="CredKart"]')

    def __init__(self, driver):
        self.driver = driver

    def getLogInLink(self):
        self.driver.find_element(*LogINPage.link_LogINButton_XPATH).click()

    def getemailAdd(self, email):
        self.driver.find_element(*LogINPage.text_Email_add_XPATH).clear()
        self.driver.find_element(*LogINPage.text_Email_add_XPATH).send_keys(email)

    def emailpassword(self, password):
        self.driver.find_element(*LogINPage.text_Password_XPATH).clear()
        self.driver.find_element(*LogINPage.text_Password_XPATH).send_keys(password)

    def getCheckRemember(self):
        self.driver.find_element(*LogINPage.check_Remember_XPATH).click()

    def getLoginButton(self):
        self.driver.find_element(*LogINPage.btn_LogINButton_XPATH).click()

    def getForgotLoginButton(self):
        self.driver.find_element(*LogINPage.btn_LogINButton_XPATH).click()

    def getMenuButton(self):
        self.driver.find_element(*LogINPage.Button_Menu_XPATH).click()

    def getLogOutButton(self):
        self.driver.find_element(*LogINPage.Button_LogOut_XPATH).click()


    def Status(self):
        try:
            self.driver.find_element(*LogINPage.Status_text_XPATH)
            return True
        except NoSuchElementException:
            return False


