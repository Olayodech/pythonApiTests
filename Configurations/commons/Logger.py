import inspect
import logging

class LOGGER():

    @staticmethod
    def log():
        logName = inspect.stack()[1][3]
        logger = logging.getLogger(logName)
        logger.setLevel(logging.debug())
        filehandler = logging.FileHandler("{0}.log".format(logName), mode="a")
        filehandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', filemode="w", datefmt='%d/%m/%y %H/%M/%S %A')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        return logger