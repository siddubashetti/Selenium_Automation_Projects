from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitHelper:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator):
        # Wait until element is visible
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator):
        # Wait until element is clickable
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url_contains(self, url_fragment):
        # Wait until URL contains a specific text
        return WebDriverWait(self.driver, self.timeout).until(
            EC.url_contains(url_fragment)
        )