from typing import Type, TypeVar, Union
from requests import Session
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from fastrpa.utils import (
    find_element,
    get_browser_options,
    get_domain,
    get_session,
)
from fastrpa.core.console import Console
from fastrpa.core.cookies import Cookies
from fastrpa.core.screenshot import Screenshot
from fastrpa.core.tabs import Tabs
from fastrpa.exceptions import ElementNotCompatibleException
from fastrpa.core.elements import (
    CheckboxElement,
    Element,
    ImageElement,
    InputElement,
    FileInputElement,
    ButtonElement,
    FormElement,
    ListElement,
    RadioInputElement,
    TableElement,
    SelectElement,
)

from fastrpa.core.wait import Wait
from fastrpa.core.keyboard import Keyboard
from fastrpa.core.elements_factory import ElementsFactory
from fastrpa.types import BrowserOptions, BrowserOptionsClass, WebDriver


SpecificElement = TypeVar('SpecificElement', bound=Element)
GenericElement = Union[Element, SpecificElement]


class Web:
    def __init__(
        self,
        webdriver: WebDriver,
        timeout: int,
    ):
        self.webdriver = webdriver
        self.timeout = timeout
        self.keyboard = Keyboard(self.webdriver)
        self.screenshot = Screenshot(self.webdriver)
        self.cookies = Cookies(self.webdriver)
        self.console = Console(self.webdriver)
        self.tabs = Tabs(self.webdriver)
        self.wait = Wait(self.webdriver, self.timeout)
        self.factory = ElementsFactory(self.webdriver, self.timeout)

    @property
    def url(self) -> str:
        return self.webdriver.current_url

    @property
    def domain(self) -> str:
        return get_domain(self.webdriver)

    @property
    def title(self) -> str:
        return self.webdriver.title

    @property
    def session(self) -> Session:
        return get_session(self.webdriver)

    def browse(self, url: str):
        self.webdriver.get(url)

    def refresh(self):
        self.webdriver.refresh()

    def is_interactive(self, xpath: str) -> bool:
        try:
            if element := self.webdriver.find_element(By.XPATH, xpath):
                return element.is_displayed()
            return False
        except NoSuchElementException:
            return False
        except StaleElementReferenceException:
            return False

    def read(self, xpath: str) -> str | None:
        try:
            if element := find_element(self.webdriver, xpath):
                return element.text if element.text else None
            return None
        except NoSuchElementException:
            return None

    def element(self, xpath: str, wait: bool = True) -> GenericElement:
        if not wait:
            return self.factory.get(xpath)
        return self.factory.get_when_available(xpath)

    def elements(self, xpath: str) -> list[GenericElement]:
        return self.factory.get_many(xpath)

    def _specific_element(
        self, xpath: str, class_name: Type[SpecificElement], wait: bool = True
    ) -> SpecificElement:
        element = self.element(xpath, wait)
        if not isinstance(element, class_name):
            raise ElementNotCompatibleException(xpath, class_name)
        return element

    def input(self, xpath: str, wait: bool = True) -> InputElement:
        return self._specific_element(xpath, InputElement, wait)

    def file_input(self, xpath: str, wait: bool = True) -> FileInputElement:
        return self._specific_element(xpath, FileInputElement, wait)

    def radio_input(self, xpath: str, wait: bool = True) -> RadioInputElement:
        return self._specific_element(xpath, RadioInputElement, wait)
    
    def checkbox(self, xpath: str, wait: bool = True) -> CheckboxElement:
        return self._specific_element(xpath, CheckboxElement, wait)
    
    def select(self, xpath: str, wait: bool = True) -> SelectElement:
        return self._specific_element(xpath, SelectElement, wait)
    
    def button(self, xpath: str, wait: bool = True) -> ButtonElement:
        return self._specific_element(xpath, ButtonElement, wait)

    def form(self, xpath: str, wait: bool = True) -> FormElement:
        return self._specific_element(xpath, FormElement, wait)

    def list(self, xpath: str, wait: bool = True) -> ListElement:
        return self._specific_element(xpath, ListElement, wait)

    def table(self, xpath: str, wait: bool = True) -> TableElement:
        return self._specific_element(xpath, TableElement, wait)

    def image(self, xpath: str, wait: bool = True) -> ImageElement:
        return self._specific_element(xpath, ImageElement, wait)


class FastRPA:
    browser_arguments = ['--start-maximized', '--ignore-certificate-errors']

    def __init__(
        self,
        webdriver: WebDriver | None = None,
        options_class: BrowserOptionsClass = ChromeOptions,
        browser_arguments: list[str] | None = None,
        timeout: int = 15,
    ):
        self._browser_options: BrowserOptions | None = None
        self._webdriver = webdriver
        self._options_class = options_class
        self.timeout = timeout

        if browser_arguments:
            self.browser_arguments = browser_arguments

    @property
    def browser_options(self) -> BrowserOptions:
        if self._browser_options is None:
            self._browser_options = get_browser_options(
                options=self.browser_arguments,
                options_class=self._options_class,
            )
        return self._browser_options

    @property
    def webdriver(self) -> WebDriver:
        if self._webdriver is None:
            self._webdriver = Remote(options=self.browser_options)
        return self._webdriver

    def __del__(self):
        self.webdriver.quit()

    def web(self, url: str | None = None) -> Web:
        obj = Web(self.webdriver, self.timeout)
        if url is not None:
            obj.browse(url)
        return obj
