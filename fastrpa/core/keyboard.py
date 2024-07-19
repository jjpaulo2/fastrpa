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

    def esc(self):
        self._press_key(Keys.ESCAPE)

    def tab(self):
        self._press_key(Keys.TAB)

    def enter(self):
        self._press_key(Keys.ENTER)

    def backspace(self):
        self._press_key(Keys.BACKSPACE)

    def home(self):
        self._press_key(Keys.HOME)

    def page_up(self):
        self._press_key(Keys.PAGE_UP)

    def page_down(self):
        self._press_key(Keys.PAGE_DOWN)
