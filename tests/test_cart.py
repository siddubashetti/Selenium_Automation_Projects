from pages.Cart_page import CartPage
from pages.login_page import LoginPage

class TestCart:

    def test_cart_page(self, driver):
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)

        # Step 1: Open the product page
        # Step 2: Login with valid credentials
        login_page.login("standard_user", "secret_sauce")

        # Step 3: Add a product to the cart
        cart_page.add_product_to_cart()

        # Step 4: Verify the cart count
        cart_counts = cart_page.get_cart_count()
        if cart_counts > 0:
            print("Cart count:", cart_counts)
            assert cart_counts == 1

        # Step 5: Remove the product from the cart
        cart_page.remove_product_from_cart()

        # Step 6: Verify the cart count is zero
        assert cart_page.is_cart_empty()