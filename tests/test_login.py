from pages.login_page import LoginPage
class TestLogin:
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)

        # Step 2: Login with valid credentials
        login_page.login("standard_user", "secret_sauce")

        # Step 3: Verify login was successful
        assert "inventory" in driver.current_url

    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)

        # Step 2: Login with valid credentials
        login_page.login("invalid_user", "invalid_password")

        # Step 3: Verify error message
        assert "Username and password do not match" in login_page.get_error_message()