from datetime import datetime
from selenium.webdriver.common.by import By
from fastrpa.exceptions import ScreenshotNotTaken
from fastrpa.types import WebDriver


class Screenshot:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    def _file_path(self, path: str | None = None) -> str:
        if path is None:
            path = f'{datetime.now().isoformat()}.png'
        return path

    def _restore_window(
        self, size: dict[str, int], position: dict[str, int], is_maximized: bool
    ):
        if not is_maximized:
            self.webdriver.set_window_size(size['width'], size['height'])
            self.webdriver.set_window_position(position['x'], position['y'])
        else:
            self.webdriver.maximize_window()

    @property
    def max_width(self) -> int:
        return self.webdriver.execute_script(
            'return document.documentElement.scrollWidth'
        )

    @property
    def max_height(self) -> int:
        return self.webdriver.execute_script(
            'return document.documentElement.scrollHeight + (window.innerHeight * 0.2)'
        )

    @property
    def is_maximized(self) -> bool:
        window_size = self.webdriver.get_window_size()
        screen_width = self.webdriver.execute_script('return screen.availWidth')
        screen_height = self.webdriver.execute_script(
            'return screen.availHeight'
        )
        return (window_size['width'] == screen_width) and (
            window_size['height'] == screen_height
        )

    @property
    def image(self) -> bytes:
        return self.webdriver.get_screenshot_as_png()

    @property
    def full_page_image(self) -> bytes:
        starter_position = self.webdriver.get_window_position()
        starter_size = self.webdriver.get_window_size()
        starter_is_maximized = self.is_maximized
        image: bytes

        try:
            self.webdriver.set_window_size(self.max_width, self.max_height)
            element = self.webdriver.find_element(By.XPATH, '//body')
            image = element.screenshot_as_png

        finally:
            self._restore_window(
                size=starter_size,
                position=starter_position,
                is_maximized=starter_is_maximized,
            )
            return image

    def save_image(self, path: str | None = None):
        success = self.webdriver.save_screenshot(self._file_path(path))
        if not success:
            raise ScreenshotNotTaken('image', self.webdriver.current_url)

    def save_full_page_image(self, path: str | None = None):
        starter_size = self.webdriver.get_window_size()
        starter_position = self.webdriver.get_window_position()
        starter_is_maximized = self.is_maximized

        try:
            self.webdriver.set_window_size(self.max_width, self.max_height)
            element = self.webdriver.find_element(By.XPATH, '//body')
            success = element.screenshot(self._file_path(path))

            if not success:
                raise ScreenshotNotTaken('image', self.webdriver.current_url)

        finally:
            self._restore_window(
                size=starter_size,
                position=starter_position,
                is_maximized=starter_is_maximized,
            )
