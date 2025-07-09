# In src/setup.py
import os
import sys
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service


def create_driver():
    """Initializes and returns a Microsoft Edge WebDriver instance."""

    # We'll use a new profile folder for Edge to keep it clean
    options = Options()
    project_path = os.getcwd()
    profile_path = os.path.join(project_path, "edge_profile")

    # --- Arguments for stability ---
    options.add_argument(f"user-data-dir={profile_path}")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")

    print("Attempting to start Microsoft Edge session...")

    try:
        # Selenium 4's built-in manager will automatically handle msedgedriver.exe
        driver = webdriver.Edge(options=options)
        print("Microsoft Edge session started successfully.")
        return driver
    except Exception as e:
        print("ERROR: Failed to create Microsoft Edge session.")
        print(f"Details: {e}")
        print("\nTROUBLESHOOTING: If this fails, please ensure Microsoft Edge is installed on your computer.")
        return None