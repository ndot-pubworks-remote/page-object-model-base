from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import PageLocators

class LoginPage(BasePage):

    def __init__(self, driver, wait, login_url):
        self.url = login_url
        self.locator = PageLocators
        super().__init__(driver, wait)

    def go_to_login_page(self):
        self.go_to_page(self.url)
        self.wait.until(EC.presence_of_element_located(self.locator.LOGIN_BOX))
        
    def check_title(self, title):
        assert self.get_title() == title