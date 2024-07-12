from time import sleep
from selenium.webdriver import Remote, ChromeOptions, ActionChains
from selenium.webdriver.common.keys import Keys
from fastrpa.commons import (
    get_element_text,
    get_browser_options,
    wait_until_element_is_hidden,
    wait_until_element_is_present,
    VISIBILITY_TIMEOUT,
)
from fastrpa.elements.form import Form
from fastrpa.types import BrowserOptions, BrowserOptionsClass, WebDriver


class Web:
    def __init__(
        self,
        url: str,
        webdriver: WebDriver,
        visibility_timeout: int,
    ):
        self.url = url
        self.webdriver = webdriver
        self.webdriver.get(url)
        self.visibility_timeout = visibility_timeout

    def reset(self):
        self.webdriver.get(self.url)

    def form(self, xpath: str) -> Form:
        return Form(xpath, self.webdriver, self.visibility_timeout)

    def read(self, xpath: str) -> str | None:
        return get_element_text(self.webdriver, xpath, self.visibility_timeout)

    def has_content(self, value: str) -> bool:
        return value in self.webdriver.page_source

    def wait_until_hide(self, xpath: str):
        wait_until_element_is_hidden(self.webdriver, xpath)

    def wait_until_present(self, xpath: str):
        wait_until_element_is_present(self.webdriver, xpath)

    def wait_seconds(self, seconds: int):
        sleep(seconds)

    def press_esc(self):
        ActionChains(self.webdriver).send_keys(Keys.ESCAPE).perform()

    def press_enter(self):
        ActionChains(self.webdriver).send_keys(Keys.ENTER).perform()

    def press_tab(self):
        ActionChains(self.webdriver).send_keys(Keys.TAB).perform()


class FastRPA:
    browser_arguments = ["--start-maximized", "--ignore-certificate-errors"]

    def __init__(
        self,
        webdriver: WebDriver | None = None,
        options_class: BrowserOptionsClass = ChromeOptions,
        browser_arguments: list[str] | None = None,
        visibility_timeout: int = VISIBILITY_TIMEOUT,
    ):
        self._browser_options: BrowserOptions | None = None
        self._webdriver = webdriver
        self._options_class = options_class
        self.visibility_timeout = visibility_timeout

        if browser_arguments:
            self.browser_arguments = browser_arguments

    @property
    def browser_options(self) -> BrowserOptions:
        if self._browser_options:
            return self._browser_options

        self._browser_options = get_browser_options(
            options=self.browser_arguments, options_class=self._options_class
        )
        return self._browser_options

    @property
    def webdriver(self) -> WebDriver:
        if self._webdriver:
            return self._webdriver

        self._webdriver = Remote(options=self.browser_options)
        return self._webdriver

    def __del__(self):
        self.webdriver.quit()

    def browse(self, url: str) -> Web:
        return Web(url, self.webdriver, self.visibility_timeout)
