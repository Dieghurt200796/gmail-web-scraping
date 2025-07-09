from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.setup import driver
# from src.setupedge import create_driver

# driver = create_driver()

driver.get("https://gmail.com")

email_selector = "tr.zE"
subject_selector = "span.bA4"

try:
    wait = WebDriverWait(driver, 30)
    unread_emails = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, email_selector)))
    for email in unread_emails:
        try:
            subject = email.find_element(By.CSS_SELECTOR, subject_selector)
            print(subject)
        except NoSuchElementException:
            pass
except TimeoutError:
    print(f"Could not find any unread emails")

driver.quit()