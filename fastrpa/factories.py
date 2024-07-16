from typing import Type
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from fastrpa.core.elements import (
    ButtonElement,
    Element,
    FileInputElement,
    FormElement,
    InputElement,
    ListElement,
    SelectElement,
    TableElement,
)
from fastrpa.exceptions import ElementNotFound, ElementNotFoundAfterTime
from fastrpa.types import WebDriver


class ElementFactory:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    def element_class(self, element: WebElement) -> Type[Element]:
        if element.tag_name in ['a', 'button']:
            return ButtonElement

        if element.tag_name in ['ol', 'ul']:
            return ListElement

        elif all(
            [element.tag_name == 'input', element.get_attribute('type') == 'file']
        ):
            return FileInputElement

        elif element.tag_name == 'input':
            return InputElement

        elif element.tag_name == 'select':
            return SelectElement

        elif element.tag_name == 'form':
            return FormElement

        elif element.tag_name == 'table':
            return TableElement

        return Element

    def get_when_available(self, xpath: str, timeout: int = 15) -> Element:
        try:
            selenium_element = WebDriverWait(self.webdriver, timeout).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath))
            )
            element_class = self.element_class(selenium_element)
            return element_class(selenium_element, self.webdriver)

        except TimeoutException:
            raise ElementNotFoundAfterTime(xpath, timeout)

    def get(self, xpath: str) -> Element:
        try:
            selenium_element = self.webdriver.find_element(By.XPATH, xpath)
            element_class = self.element_class(selenium_element)
            return element_class(selenium_element, self.webdriver)

        except NoSuchElementException:
            raise ElementNotFound(xpath)
