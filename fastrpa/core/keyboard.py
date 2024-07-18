from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from fastrpa.types import WebDriver


class Keyboard:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver
        self.actions = ActionChains(self.webdriver)

    def _press_key(self, key: str):
        self.actions.send_keys(key)
        self.actions.perform()

    def press_esc(self):
        self._press_key(Keys.ESCAPE)

    def press_tab(self):
        self._press_key(Keys.TAB)

    def press_enter(self):
        self._press_key(Keys.ENTER)
