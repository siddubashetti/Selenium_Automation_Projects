from selenium.webdriver.common.by import By
from utils.wait_helper import WaitHelper

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    # Locators
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")
    ORDER_CONFIRMATION = (By.CLASS_NAME, "complete-header")


    def proceed_to_checkout(self):
        self.wait.wait_for_element_clickable(self.CHECKOUT_BUTTON).click()

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.wait.wait_for_element_clickable(self.FIRST_NAME).send_keys(first_name)
        self.wait.wait_for_element_clickable(self.LAST_NAME).send_keys(last_name)
        self.wait.wait_for_element_clickable(self.POSTAL_CODE).send_keys(postal_code)
        self.wait.wait_for_element_clickable(self.CONTINUE_BUTTON).click()

    def get_checkout_title(self):
        title = self.wait.wait_for_element_visible(self.TITLE).text
        return title

    def finish_checkout(self):
        self.wait.wait_for_element_clickable(self.FINISH_BUTTON).click()

    def get_order_confirmation(self):
        return self.wait.wait_for_element_visible(self.ORDER_CONFIRMATION).text