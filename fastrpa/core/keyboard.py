from fastrpa.types import WebDriver, Keys, ActionChains


class Keyboard:

    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    def _press_key(self, key: str):
        action = ActionChains(self.webdriver)
        action.send_keys(key)
        action.perform()

    def press_esc(self):
        self._press_key(Keys.ESCAPE)
    
    def press_tab(self):
        self._press_key(Keys.TAB)

    def press_enter(self):
        self._press_key(Keys.ENTER)
