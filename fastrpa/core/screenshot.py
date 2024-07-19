from datetime import datetime
from selenium.webdriver.common.by import By
from fastrpa.types import WebDriver


class Screenshot:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    def _file_path(self, path: str | None = None) -> str:
        if path is None:
            path = f'{datetime.now().isoformat()}.png'
        return path

    @property
    def max_width(self) -> int:
        return self.webdriver.execute_script('return document.documentElement.scrollWidth')

    @property
    def max_height(self) -> int:
        return self.webdriver.execute_script(
            'return document.documentElement.scrollHeight + (window.innerHeight * 0.2)'
        )

    def viewport(self, path: str | None = None):
        self.webdriver.save_screenshot(self._file_path(path))

    def full_page(self, path: str | None = None):
        starter_position = self.webdriver.get_window_position()
        starter_size = self.webdriver.get_window_size()

        try:
            self.webdriver.set_window_size(self.max_width, self.max_height)
            self.webdriver.find_element(By.XPATH, '//body').screenshot(self._file_path(path))

        finally:
            self.webdriver.set_window_size(starter_size['width'], starter_size['height'])
            self.webdriver.set_window_position(starter_position['x'], starter_position['y'])
