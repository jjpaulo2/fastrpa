from time import sleep

from fastrpa.commons import wait_until_element_is_hidden, wait_until_element_is_present
from fastrpa.types import WebDriver


class Timer:

    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    def wait_until_hide(self, xpath: str):
        wait_until_element_is_hidden(self.webdriver, xpath)

    def wait_until_present(self, xpath: str):
        wait_until_element_is_present(self.webdriver, xpath)

    def wait_seconds(self, seconds: int):
        sleep(seconds)
