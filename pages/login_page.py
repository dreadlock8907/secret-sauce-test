import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    
    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '[data-test="error"]'

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Open login page")
    def open(self) -> None:
        self.navigate_to(self.URL)

    @allure.step("Enter username: {username}")
    def enter_username(self, username: str) -> None:
        self.page.fill(self.USERNAME_INPUT, username)

    @allure.step("Enter password")
    def enter_password(self, password: str) -> None:
        self.page.fill(self.PASSWORD_INPUT, password)

    @allure.step("Click login button")
    def click_login_button(self) -> None:
        self.page.click(self.LOGIN_BUTTON)

    @allure.step("Login with credentials: {username}")
    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Get error message")
    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

    @allure.step("Check if error message is displayed")
    def is_error_message_displayed(self) -> bool:
        return self.is_element_visible(self.ERROR_MESSAGE)

    @allure.step("Check if login button is displayed")
    def is_login_button_displayed(self) -> bool:
        return self.is_element_visible(self.LOGIN_BUTTON)
