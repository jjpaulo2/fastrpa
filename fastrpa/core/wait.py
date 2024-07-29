from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from fastrpa.types import WebDriver


class Wait:
    def __init__(self, webdriver: WebDriver, timeout: float):
        self._timeout = timeout
        self.webdriver = webdriver

    def get_timeout(self, value: float | None) -> float:
        if value is not None:
            return value
        return self._timeout

    def source(self, timeout: float | None = None) -> WebDriverWait:
        return WebDriverWait(self.webdriver, self.get_timeout(timeout))

    def seconds(self, seconds: float):
        sleep(seconds)

    def is_present(self, xpath: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def not_is_present(self, xpath: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until_not(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def is_clickable(self, xpath: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

    def not_is_clickable(self, xpath: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until_not(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

    def is_hidden(self, xpath: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until(
            EC.invisibility_of_element_located((By.XPATH, xpath))
        )

    def not_is_hidden(self, xpath: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until_not(
            EC.invisibility_of_element_located((By.XPATH, xpath))
        )

    def contains_text(
        self, xpath: str, text: str, timeout: float | None = None
    ):
        self.source(self.get_timeout(timeout)).until(
            EC.text_to_be_present_in_element((By.XPATH, xpath), text)
        )

    def not_contains_text(
        self, xpath: str, text: str, timeout: float | None = None
    ):
        self.source(self.get_timeout(timeout)).until_not(
            EC.text_to_be_present_in_element((By.XPATH, xpath), text)
        )

    def url_contains(self, sub_url: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until(EC.url_contains(sub_url))

    def not_url_contains(self, sub_url: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until_not(
            EC.url_contains(sub_url)
        )

    def title_contains(self, sub_title: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until(
            EC.title_contains(sub_title)
        )

    def not_title_contains(self, sub_title: str, timeout: float | None = None):
        self.source(self.get_timeout(timeout)).until_not(
            EC.title_contains(sub_title)
        )
