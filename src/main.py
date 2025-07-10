import dotenv
import logging
import logging.config
import sys

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import src.setup as setup
from src.login import login

logging.config.fileConfig('logging.conf')

def get_subjects(driver):
    logging.info("Navigating to Gmail...")
    try:
        # NOTE: These may change in future. Use HTML inspections to try
        # and find a class name that is unique to unread emails and subject lines.
        unread_email_selector = "tr.zE"
        subject_selector = "span.bog"

        wait = WebDriverWait(driver, 30)
        unread_emails = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, unread_email_selector)))
        logging.info(f"Found {len(unread_emails)} unread emails.")
    except Exception as e:
        logging.warning(f"Could not find unread emails. Check your selector or if you have unread mail. Error: {e}")
        return

    print("\n--- Unread Email Subjects ---")
    for email in unread_emails:
        try:
            subject = email.find_element(By.CSS_SELECTOR, subject_selector)
            subject_text = subject.text
            if subject_text:
                print(subject_text)
        except Exception:
            pass

def main():
    if not setup.driver:
        logging.warning("No driver found.")
        sys.exit(1)

    try:
        login_var = login()

        if login_var:
            get_subjects(setup.driver)
        else:
            logging.warning("Login failed. Cannot extract emails.")

    except Exception as e:
        logging.warning(f"An unexpected error occurred: {e}")
    finally:
        setup.driver.quit()

# dotenv.load_dotenv()
#
# driver.get("https://gmail.com")
#
# # These may change in future. Use HTML inspections to try
# # and find a class name that is unique to unread emails and subject lines.
# email_selector = "tr.zE"
# subject_selector = "span.bog"
#
# try:
#     wait = WebDriverWait(driver, 10)
#     unread_emails = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, email_selector)))
#     for email in unread_emails:
#         try:
#             subject = email.find_element(By.CSS_SELECTOR, subject_selector)
#             print(subject.text)
#         except NoSuchElementException:
#             pass
# except TimeoutError:
#     print(f"Could not find any unread emails")
#
# driver.quit()

main()