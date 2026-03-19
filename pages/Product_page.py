from selenium.webdriver.common.by import By
from utils.wait_helper import WaitHelper

class Productspage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    # Locators
    PAGE_TITLE = (By.XPATH, "//span[@class='title']")
    PRODUCTS_COUNT = (By.CLASS_NAME, "inventory_item")
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_DETAIL_TITLE = (By.CSS_SELECTOR, ".inventory_details_name")

    def get_page_title(self):
        return self.wait.wait_for_element_visible(self.PAGE_TITLE).text
    
    def get_products_count(self):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        return len(products)
    
    def click_product(self):
        # Click the first product
        self.wait.wait_for_element_clickable(self.FIRST_PRODUCT).click()

    def get_product_detail_title(self):
        # Get the product title on detail page
        return self.wait.wait_for_element_visible(self.PRODUCT_DETAIL_TITLE).text

