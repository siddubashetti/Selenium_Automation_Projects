from pages.CheckoutPage import CheckoutPage
from pages.login_page import LoginPage
from pages.Cart_page import CartPage

class TestCheckout:

    def test_checkout_page(self, driver):
        checkout_page = CheckoutPage(driver)
        login_page = LoginPage(driver)
        cart_page = CartPage(driver)

        # Step 1: Open the product page
        # Step 2: Login with valid credentials
        login_page.login("standard_user", "secret_sauce")

        # Step 3: Add a product to the cart
        cart_page.add_product_to_cart()

        # Step 4: Verify the cart 
        cart_page.proceed_to_cart()
        print("URL after cart:", driver.current_url)  
        
        # Step 4: Proceed to checkout
        checkout_page.proceed_to_checkout()
        print("URL after checkout click:", driver.current_url)

        # Step 5: Fill in checkout information
        checkout_page.fill_checkout_information("John", "Doe", "12345")

        # Step 6: Verify checkout overview page
        assert "Checkout: Overview" in checkout_page.get_checkout_title()

        # Step 7: Finish checkout
        checkout_page.finish_checkout()
        assert "Thank you for your order!" in checkout_page.get_order_confirmation()