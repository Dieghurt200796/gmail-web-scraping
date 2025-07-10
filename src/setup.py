import logging
import logging.config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.config.fileConfig('logging.conf')

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")

try:
    driver = webdriver.Chrome(options=options)
    logging.info("Chrome session started successfully.")
except Exception as e:
    logging.info(f"ERROR: Failed to create Chrome session. Details: {e}")
    driver = None
