
from selenium import webdriver
from selenium.webdriver.common.by import By


class Registration:
    btn_Registration_XPATH=(By.XPATH,"//a[text()='Register']")
    xx='//a[text()="Register"]'
    text_Name_XPATH=(By.XPATH,"//input[@id='name']")
    text_E_Mail_Address_XPATH=(By.XPATH,'//input[@id="email"]')
    text_Password_XPATH=(By.XPATH,"//input[@id='password']")
    text_Confirm_Password_XPATH=(By.XPATH,'//input[@id="password-confirm"]')
    click_Register_XPATH=(By.XPATH,'//button[@type="submit"]')
    Exp_title='CredKart'

    def __init__(self,driver):
        self.driver=driver

    def getegistrationlink(self):
        self.driver.find_element(*Registration.btn_Registration_XPATH).click()
        # self.driver.find_element(By.XPATH,self.xx).click()

    def getReg_Name(self,Username):
        self.driver.find_element(*Registration.text_Name_XPATH).clear()
        self.driver.find_element(*Registration.text_Name_XPATH).send_keys(Username)

    def getEmaliadd(self,email):
        self.driver.find_element(*Registration.text_E_Mail_Address_XPATH).clear()
        self.driver.find_element(*Registration.text_E_Mail_Address_XPATH).send_keys(email)

    def getPassword(self,password):
        self.driver.find_element(*Registration.text_Password_XPATH).clear()
        self.driver.find_element(*Registration.text_Password_XPATH).send_keys(password)

    def getConfPassword(self,Confirmpass):
        self.driver.find_element(*Registration.text_Confirm_Password_XPATH).clear()
        self.driver.find_element(*Registration.text_Confirm_Password_XPATH).send_keys(Confirmpass)

    def getRegistrationButton(self):
        self.driver.find_element(*Registration.click_Register_XPATH).click()














