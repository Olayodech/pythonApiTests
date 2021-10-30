import logging
from fileinput import filename

logging.basicConfig(filename='%(asctime)s: %(levelname)s: %(messahe)s', filemode="w", datefmt='%d/%m/%y %H/%M/%S %A', level=logging.DEBUG)
logging.critical("")
logging.debug("")
logging.warning("")
logging.info("")
logging.error("")