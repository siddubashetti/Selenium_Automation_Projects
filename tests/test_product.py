from pages.Product_page import Productspage
from pages.login_page import LoginPage

class TestProduct:
    def test_product_page(self, driver):
        product_page = Productspage(driver)
        login_page = LoginPage(driver)

        # Step 1: Open the product page
        # Step 2: Login with valid credentials
        login_page.login("standard_user", "secret_sauce")

        title = product_page.get_page_title()
        assert title == "Products"

        products_count = product_page.get_products_count()
        print("Products count:", products_count)
        assert products_count == 6

        product_page.click_product()

        detail_title = product_page.get_product_detail_title()
        print("Product detail title:", detail_title)
        assert detail_title is not None
