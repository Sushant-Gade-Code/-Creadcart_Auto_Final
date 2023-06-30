import configparser

config=configparser.RawConfigParser()
config.read('C:\\Users\\Admin\\PycharmProjects\\CreadCart_Auto_final\\Configuration\\config.ini')

class ReadProperties:

    @staticmethod
    def getBaseUrl():
        bseurl=config.get("LogIn Info","baseUrl")
        return bseurl

    @staticmethod
    def getemail():
        email = config.get("LogIn Info", "email")
        return email

    @staticmethod
    def getpassword():
        password = config.get("LogIn Info", "password")
        return password

    @staticmethod
    def geteNameR():
        nameR = config.get("Regi InFo", "name")
        return nameR

    @staticmethod
    def getemailR():
        emailR = config.get("Regi InFo", "email")
        return emailR

    @staticmethod
    def getepasswordR():
        passwordR = config.get("Regi InFo", "password")
        return passwordR

    @staticmethod
    def geteconfirmPassR():
        confirmPassR = config.get("Regi InFo", "confirmPass")
        return  confirmPassR




