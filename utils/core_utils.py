import gettext
import locale
import logging
from core.constants import Env
from logging.handlers import RotatingFileHandler

locales_dir = Env.SCRIPT_PATH / "locales"

class LoggerSetup:
    @staticmethod
    def initialize():
        """
        Set up the logger for usage in logging over prints
        Logs to astrostack.log in same dir as .py
        Is rotating (At 100kb size on new creation)
        """
        handler = RotatingFileHandler(
            "astrostack.log", 
            maxBytes=10**5,
            backupCount=3
            )
        
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[handler]
        )
        logger = logging.getLogger(__name__)
        logger.info("Logger initialized")