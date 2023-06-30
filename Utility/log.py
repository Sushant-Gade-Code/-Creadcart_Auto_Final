import inspect
import logging


class LogGenerator:

    @staticmethod
    def loggen():
        name=inspect.stack()[1][3]
        logger=logging.getLogger(name)
        File=logging.FileHandler(".\\Logs\\Creadcartlog.log")
        Format=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        File.setFormatter(Format)
        logger.addHandler(File)
        logger.setLevel(logging.DEBUG)
        return logger

