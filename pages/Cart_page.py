from selenium.webdriver.common.by import By
from utils.wait_helper import WaitHelper

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    # Locators
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")
    REMOVE_FROM_CART = (By.ID, "remove-sauce-labs-backpack")


    def add_product_to_cart(self):
        self.wait.wait_for_element_clickable(self.ADD_TO_CART).click()

    def proceed_to_cart(self):
        self.wait.wait_for_element_clickable(self.CART_LINK).click()

    def get_cart_count(self):
        cart_count = self.wait.wait_for_element_visible(self.CART_COUNT).text
        return int(cart_count)

    def remove_product_from_cart(self):
        self.wait.wait_for_element_clickable(self.REMOVE_FROM_CART).click()

    def is_cart_empty(self):
        # Use find_elements - returns empty list if not found, no error!
        cart_items = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return len(cart_items) == 0

    
