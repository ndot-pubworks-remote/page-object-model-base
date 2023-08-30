import os
import datetime
from dotenv import load_dotenv
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
    
from pages.login_page import LoginPage

driver = webdriver.Firefox()

dotenv_path = Path('data/.env')
load_dotenv(dotenv_path = dotenv_path)
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

login = LoginPage(driver, WebDriverWait(driver, 35))