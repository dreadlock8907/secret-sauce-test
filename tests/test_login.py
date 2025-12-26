import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Authentication")
@allure.story("User Login")
@pytest.mark.login
class TestLogin:

    @allure.title("Successful login with standard user")
    @allure.description("Test successful authentication with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.crit
    def test_successful_login(self, login_page: LoginPage, inventory_page: InventoryPage):
        with allure.step("Open login page"):
            login_page.open()
            assert login_page.is_login_button_displayed()

        with allure.step("Login with valid credentials"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Verify redirect to inventory page"):
            assert inventory_page.is_page_loaded()

        with allure.step("Verify URL"):
            assert inventory_page.verify_url()

        with allure.step("Verify page elements"):
            assert inventory_page.is_inventory_list_displayed()
            assert inventory_page.is_shopping_cart_displayed()
            assert inventory_page.is_burger_menu_displayed()
            assert inventory_page.get_page_title() == "Products"

        with allure.step("Verify items are present"):
            items_count = inventory_page.get_inventory_items_count()
            assert items_count > 0
            allure.attach(str(items_count), name="Items count", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Login with invalid password")
    @allure.description("Test error message display with incorrect password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.crit
    def test_login_with_invalid_password(self, login_page: LoginPage):
        with allure.step("Open login page"):
            login_page.open()

        with allure.step("Login with invalid password"):
            login_page.login("standard_user", "wrong_password")

        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed()
            error_text = login_page.get_error_message()
            allure.attach(error_text, name="Error text", attachment_type=allure.attachment_type.TEXT)
            assert "Username and password do not match" in error_text

        with allure.step("Verify user stays on login page"):
            assert login_page.get_current_url() == login_page.URL
            assert login_page.is_login_button_displayed()

    @allure.title("Login with locked out user")
    @allure.description("Test access denial for locked out user")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.crit
    def test_locked_out_user_login(self, login_page: LoginPage):
        with allure.step("Open login page"):
            login_page.open()

        with allure.step("Login with locked out user"):
            login_page.login("locked_out_user", "secret_sauce")

        with allure.step("Verify lockout message is displayed"):
            assert login_page.is_error_message_displayed()
            error_text = login_page.get_error_message()
            allure.attach(error_text, name="Error text", attachment_type=allure.attachment_type.TEXT)
            assert "this user has been locked out" in error_text.lower()

        with allure.step("Verify access is denied"):
            assert login_page.get_current_url() == login_page.URL
            assert login_page.is_login_button_displayed()

    @allure.title("Login with empty fields")
    @allure.description("Test validation with empty credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_fields(self, login_page: LoginPage):
        with allure.step("Open login page"):
            login_page.open()

        with allure.step("Click login without entering credentials"):
            login_page.click_login_button()

        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed()
            error_text = login_page.get_error_message()
            allure.attach(error_text, name="Error text", attachment_type=allure.attachment_type.TEXT)
            assert "Username is required" in error_text

        with allure.step("Verify user stays on login page"):
            assert login_page.get_current_url() == login_page.URL

    @allure.title("Login with performance_glitch_user")
    @allure.description("Test successful login with performance delays")
    @allure.severity(allure.severity_level.NORMAL)
    def test_performance_glitch_user_login(self, login_page: LoginPage, inventory_page: InventoryPage):
        with allure.step("Open login page"):
            login_page.open()

        with allure.step("Login with performance_glitch_user"):
            login_page.login("performance_glitch_user", "secret_sauce")

        with allure.step("Wait for inventory page to load (with extended timeout)"):
            assert inventory_page.is_page_loaded(timeout=30000)

        with allure.step("Verify URL"):
            assert inventory_page.verify_url()

        with allure.step("Verify page elements"):
            assert inventory_page.is_inventory_list_displayed()
            assert inventory_page.is_shopping_cart_displayed()
            assert inventory_page.get_page_title() == "Products"

        with allure.step("Verify items are present"):
            items_count = inventory_page.get_inventory_items_count()
            assert items_count > 0
            allure.attach(str(items_count), name="Items count", attachment_type=allure.attachment_type.TEXT)
