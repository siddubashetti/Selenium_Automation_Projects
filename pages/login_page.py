from selenium.webdriver.common.by import By
from utils.wait_helper import WaitHelper

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON   = (By.ID, "login-button")
    ERROR_MESSAGE  = (By.XPATH, "//h3[@data-test='error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.open()
        # Using explicit wait instead of find_element directly
        self.wait.wait_for_element_visible(self.USERNAME_FIELD).send_keys(username)
        self.wait.wait_for_element_visible(self.PASSWORD_FIELD).send_keys(password)
        self.wait.wait_for_element_clickable(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.wait.wait_for_element_visible(self.ERROR_MESSAGE).text