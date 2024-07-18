from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from fastrpa.types import WebDriver


class Timer:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    def wait_until_hide(self, xpath: str, timeout_seconds: int = 15):
        WebDriverWait(self.webdriver, timeout_seconds).until_not(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath))
        )

    def wait_until_present(self, xpath: str, timeout_seconds: int = 15):
        WebDriverWait(self.webdriver, timeout_seconds).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath))
        )

    def wait_seconds(self, seconds: int):
        sleep(seconds)
