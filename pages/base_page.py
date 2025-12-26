from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str) -> None:
        self.page.goto(url)

    def get_current_url(self) -> str:
        return self.page.url

    def is_element_visible(self, selector: str, timeout: int = 5000) -> bool:
        try:
            self.page.wait_for_selector(selector, state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    def wait_for_url(self, url: str, timeout: int = 30000) -> None:
        self.page.wait_for_url(url, timeout=timeout)
