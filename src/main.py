from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.setup import driver

# driver = create_driver()

# C:\Users\EM2025008152\AppData\Local\Google\Chrome\User Data\Default

driver.get("https://gmail.com")

# These may change in future. Use HTML inspections to try
# and find a class name that is unique to unread emails and subject lines.
email_selector = "tr.zE"
subject_selector = "span.bog"

try:
    wait = WebDriverWait(driver, 10)
    unread_emails = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, email_selector)))
    for email in unread_emails:
        try:
            subject = email.find_element(By.CSS_SELECTOR, subject_selector)
            print(subject.text)
        except NoSuchElementException:
            pass
except TimeoutError:
    print(f"Could not find any unread emails")

driver.quit()