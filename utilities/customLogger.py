import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'

        logging.basicConfig(
            filename=path,
            level=logging.DEBUG,  # Set logging level to DEBUG
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'  # Date and time format
        )

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

