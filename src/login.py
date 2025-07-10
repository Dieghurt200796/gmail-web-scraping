import logging
import logging.config
import dotenv
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.setup import driver

logging.config.fileConfig('logging.conf')

def login():
    dotenv.load_dotenv()
    email = os.getenv("GMAIL_EMAIL")
    password = os.getenv("GMAIL_PASSWORD")
    logging.debug(f"Looking for .env file in this directory: {os.getcwd()}")
    logging.debug(f"GMAIL_EMAIL variable found: {os.getenv('GMAIL_EMAIL')}")
    logging.debug(f"GMAIL_APP_PASSWORD variable found: {os.getenv('GMAIL_PASSWORD')}")

    if not email or not password:
        raise ValueError("Email or App Password not found in .env file.")

    try:
        logging.info("Navigating to Google login page...")
        driver.get("https://mail.google.com/")

        # --- Enter Email ---
        wait = WebDriverWait(driver, 15)
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "identifierId")))
        email_field.send_keys(email)
        driver.find_element(By.ID, "identifierNext").click()
        logging.info("Email entered.")

        password_field = wait.until(EC.element_to_be_clickable((By.NAME, "Passwd")))
        time.sleep(1)
        password_field.send_keys(password)
        driver.find_element(By.ID, "passwordNext").click()
        logging.info("Password entered.")

        # Wait until the login is fully complete by checking for a known element
        # on the account page, like the profile icon.
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Google Account']")))
        return True

    except Exception as e:
        logging.error(f"ERROR: An error occurred during login: {e}")
        driver.save_screenshot("login_error.png")
        logging.error("Screenshot of error saved.")
        return False