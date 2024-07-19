from typing import Type, TypeVar
from selenium.webdriver import Remote, ChromeOptions
from fastrpa.commons import (
    get_browser_options,
    get_domain,
)
from fastrpa.core.cookies import Cookies
from fastrpa.core.screenshot import Screenshot
from fastrpa.exceptions import ElementNotCompatible
from fastrpa.settings import DEFAULT_TIMEOUT
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
from fastrpa.factory import ElementFactory
from fastrpa.types import BrowserOptions, BrowserOptionsClass, WebDriver


SpecificElement = TypeVar('SpecificElement', bound=Element)


class Web:
    def __init__(
        self,
        url: str,
        webdriver: WebDriver,
        timeout_seconds: int,
    ):
        self.starter_url = url
        self.webdriver = webdriver
        self.webdriver.get(self.starter_url)
        self.timeout_seconds = timeout_seconds
        self.keyboard = Keyboard(self.webdriver)
        self.timer = Timer(self.webdriver)
        self.screenshot = Screenshot(self.webdriver)
        self.cookies = Cookies(self.webdriver)
        self.factory = ElementFactory(self.webdriver)

    @property
    def url(self) -> str:
        return self.webdriver.current_url

    @property
    def domain(self) -> str:
        return get_domain(self.webdriver)

    def browse(self, url: str):
        self.webdriver.get(url)
    
    def refresh(self):
        self.webdriver.refresh()

    def reset(self):
        self.webdriver.get(self.starter_url)

    def element(self, xpath: str, wait: bool = True) -> Element | SpecificElement:
        if not wait:
            return self.factory.get(xpath)
        return self.factory.get_when_available(xpath, self.timeout_seconds)

    def elements(self, xpath: str) -> list[Element | SpecificElement]:
        return self.factory.get_many(xpath)

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
        timeout_seconds: int = DEFAULT_TIMEOUT,
    ):
        self._browser_options: BrowserOptions | None = None
        self._webdriver = webdriver
        self._options_class = options_class
        self.timeout_seconds = timeout_seconds

        if browser_arguments:
            self.browser_arguments = browser_arguments

    @property
    def browser_options(self) -> BrowserOptions:
        if self._browser_options is None:
            self._browser_options = get_browser_options(
                options=self.browser_arguments, options_class=self._options_class
            )
        return self._browser_options

    @property
    def webdriver(self) -> WebDriver:
        if self._webdriver is None:
            self._webdriver = Remote(options=self.browser_options)
        return self._webdriver

    def __del__(self):
        self.webdriver.quit()

    def browse(self, url: str) -> Web:
        return Web(url, self.webdriver, self.timeout_seconds)
