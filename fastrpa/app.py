from typing import Type, TypeVar
from selenium.webdriver import Remote, ChromeOptions
from fastrpa.commons import (
    get_browser_options,
)
from fastrpa.core.screenshot import Screenshot
from fastrpa.exceptions import ElementNotCompatible
from fastrpa.settings import VISIBILITY_TIMEOUT
from fastrpa.core.elements import (
    Element,
    InputElement,
    FileInputElement,
    ButtonElement,
    FormElement,
    ListElement,
    TableElement,
    SelectElement,
)

from fastrpa.core.timer import Timer
from fastrpa.core.keyboard import Keyboard
from fastrpa.factories import ElementFactory
from fastrpa.types import BrowserOptions, BrowserOptionsClass, WebDriver


SpecificElement = TypeVar('SpecificElement', bound=Element)


class Web:
    def __init__(
        self,
        url: str,
        webdriver: WebDriver,
        visibility_timeout: int,
    ):
        self._keyboard: Keyboard | None = None
        self._timer: Timer | None = None
        self._screenshot: Screenshot | None = None
        self.starter_url = url
        self.webdriver = webdriver
        self.webdriver.get(self.starter_url)
        self._element_factory = ElementFactory(self.webdriver)
        self.visibility_timeout = visibility_timeout

    @property
    def url(self) -> str:
        return self.webdriver.current_url

    @property
    def keyboard(self) -> Keyboard:
        if self._keyboard is None:
            self._keyboard = Keyboard(self.webdriver)
        return self._keyboard

    @property
    def timer(self) -> Timer:
        if self._timer is None:
            self._timer = Timer(self.webdriver)    
        return self._timer
    
    @property
    def screenshot(self) -> Screenshot:
        if self._screenshot is None:
            self._screenshot = Screenshot(self.webdriver)
        return self._screenshot

    def reset(self):
        self.webdriver.get(self.starter_url)

    def has_content(self, value: str) -> bool:
        return value in self.webdriver.page_source

    def element(self, xpath: str, wait: bool = True) -> Element | SpecificElement:
        if not wait:
            return self._element_factory.get(xpath)
        return self._element_factory.get_when_available(xpath, self.visibility_timeout)

    def _specific_element(
        self, xpath: str, class_name: Type[SpecificElement], wait: bool = True
    ) -> SpecificElement:
        element = self.element(xpath, wait)
        if not isinstance(element, class_name):
            raise ElementNotCompatible(xpath, class_name)
        return element

    def input(self, xpath: str, wait: bool = True) -> InputElement:
        return self._specific_element(xpath, InputElement, wait)

    def file_input(self, xpath: str, wait: bool = True) -> FileInputElement:
        return self._specific_element(xpath, FileInputElement, wait)

    def button(self, xpath: str, wait: bool = True) -> ButtonElement:
        return self._specific_element(xpath, ButtonElement, wait)

    def form(self, xpath: str, wait: bool = True) -> FormElement:
        return self._specific_element(xpath, FormElement, wait)

    def select(self, xpath: str, wait: bool = True) -> SelectElement:
        return self._specific_element(xpath, SelectElement, wait)

    def list(self, xpath: str, wait: bool = True) -> ListElement:
        return self._specific_element(xpath, ListElement, wait)

    def table(self, xpath: str, wait: bool = True) -> TableElement:
        return self._specific_element(xpath, TableElement, wait)


class FastRPA:
    browser_arguments = ['--start-maximized', '--ignore-certificate-errors']

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
