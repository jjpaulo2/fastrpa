from typing import Type
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from fastrpa.core.elements import (
    ButtonElement,
    CheckboxElement,
    Element,
    FileInputElement,
    FormElement,
    ImageElement,
    InputElement,
    ListElement,
    RadioInputElement,
    SelectElement,
    TableElement,
)
from fastrpa.utils import ensure_element
from fastrpa.exceptions import ElementNotFoundException, ElementTimeoutException
from fastrpa.types import WebDriver


class ElementsFactory:
    def __init__(self, webdriver: WebDriver, timeout: int):
        self.timeout = timeout
        self.webdriver = webdriver

    def element_class(self, element: WebElement) -> Type[Element]:
        if element.tag_name in ['a', 'button']:
            return ButtonElement

        if element.tag_name in ['ol', 'ul']:
            return ListElement

        elif all(
            [
                element.tag_name == 'input',
                element.get_attribute('type') == 'file',
            ]
        ):
            return FileInputElement
        
        elif all(
            [
                element.tag_name == 'input',
                element.get_attribute('type') == 'radio',
            ]
        ):
            return RadioInputElement
        
        elif all(
            [
                element.tag_name == 'input',
                element.get_attribute('type') == 'checkbox',
            ]
        ):
            return CheckboxElement

        elif element.tag_name in ['input', 'textarea']:
            return InputElement

        elif element.tag_name == 'select':
            return SelectElement

        elif element.tag_name == 'form':
            return FormElement

        elif element.tag_name == 'table':
            return TableElement

        elif element.tag_name == 'img':
            return ImageElement

        return Element

    @ensure_element
    def get_when_available(self, xpath: str) -> Element:
        try:
            selenium_element = WebDriverWait(
                self.webdriver, self.timeout
            ).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, xpath)
                )
            )
            element_class = self.element_class(selenium_element)
            return element_class(xpath, self.webdriver)

        except TimeoutException:
            raise ElementTimeoutException(xpath, self.timeout)

    @ensure_element
    def get(self, xpath: str) -> Element:
        try:
            selenium_element = self.webdriver.find_element(By.XPATH, xpath)
            element_class = self.element_class(selenium_element)
            return element_class(xpath, self.webdriver)

        except NoSuchElementException:
            raise ElementNotFoundException(xpath)

    @ensure_element
    def get_many(self, xpath: str) -> list[Element]:
        elements_to_return = []

        try:
            for selenium_element in self.webdriver.find_elements(
                By.XPATH, xpath
            ):
                element_class = self.element_class(selenium_element)
                elements_to_return.append(element_class(xpath, self.webdriver))

            return elements_to_return

        except NoSuchElementException:
            raise ElementNotFoundException(xpath)
