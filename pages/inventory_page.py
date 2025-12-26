import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"
    
    INVENTORY_CONTAINER = '.inventory_container'
    INVENTORY_LIST = '.inventory_list'
    INVENTORY_ITEM = '.inventory_item'
    SHOPPING_CART = '.shopping_cart_link'
    BURGER_MENU = '#react-burger-menu-btn'
    PAGE_TITLE = '.title'

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Check if inventory page is loaded")
    def is_page_loaded(self, timeout: int = 30000) -> bool:
        return self.is_element_visible(self.INVENTORY_CONTAINER, timeout=timeout)

    @allure.step("Check if inventory list is displayed")
    def is_inventory_list_displayed(self) -> bool:
        return self.is_element_visible(self.INVENTORY_LIST)

    @allure.step("Get inventory items count")
    def get_inventory_items_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEM).count()

    @allure.step("Check if shopping cart is displayed")
    def is_shopping_cart_displayed(self) -> bool:
        return self.is_element_visible(self.SHOPPING_CART)

    @allure.step("Check if burger menu is displayed")
    def is_burger_menu_displayed(self) -> bool:
        return self.is_element_visible(self.BURGER_MENU)

    @allure.step("Get page title")
    def get_page_title(self) -> str:
        return self.page.locator(self.PAGE_TITLE).inner_text()

    @allure.step("Verify URL")
    def verify_url(self) -> bool:
        return self.get_current_url() == self.URL
