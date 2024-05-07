import logging
import os

def setup_logger():
    logging_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logging.basicConfig(level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)
