from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Input and clean path
path = input("Enter Chrome Profile Path: ").strip()
path = path.replace("\\", "/")  # Fix backslashes

if not os.path.exists(path):
    print("Error: Provided path does not exist.")
    exit()

options = Options()
options.add_argument(f"--user-data-dir={path}")
options.add_argument("--profile-directory=Default")

# Optional args
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())

try:
    driver = webdriver.Chrome(service=service, options=options)
    print("Chrome session started successfully.")
except Exception as e:
    print("Failed to create Chrome session.")
    print(f"Error: {e}")
    driver = None
