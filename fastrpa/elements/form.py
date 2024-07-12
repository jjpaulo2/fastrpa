from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from fastrpa.commons import (
    get_element,
    get_select_element,
    get_file_path,
)
from fastrpa.dataclasses import Item, Option
from fastrpa.types import WebDriver


class Form:
    def __init__(self, xpath: str, webdriver: WebDriver, visibility_timeout: int):
        self._element: WebElement | None = None
        self.xpath = xpath
        self.webdriver = webdriver
        self.visibility_timeout = visibility_timeout

    @property
    def element(self) -> WebElement:
        return get_element(self.webdriver, self.xpath, self.visibility_timeout)

    def _get_child_element(self, xpath: str) -> WebElement:
        return get_element(self.element, xpath, self.visibility_timeout)

    def fill(self, xpath: str, value: str):
        input_element = self._get_child_element(xpath)
        input_element.send_keys(value)

    def click(self, xpath: str):
        action = ActionChains(self.webdriver)
        action.click(self._get_child_element(xpath))
        action.perform()

    def attach_file(self, xpath: str, path: str):
        input_element = self._get_child_element(xpath)
        input_element.send_keys(get_file_path(path))

    def get_select_options(self, xpath: str) -> list[Option]:
        select_element = self._get_child_element(xpath)
        options_list = select_element.find_elements(By.XPATH, "./option")
        return [
            Option(option.get_attribute("value"), option.get_attribute("innerText"))
            for option in options_list
        ]

    def select_option(
        self, xpath: str, label: str | None = None, value: str | None = None
    ):
        select_element = get_select_element(
            self.element, xpath, self.visibility_timeout
        )
        if label:
            select_element.select_by_visible_text(label)
        elif value:
            select_element.select_by_value(value)
        else:
            raise ValueError('You must provide at least "label" or "value"!')

    def get_list_items(self, xpath: str) -> list[Item]:
        list_element = self._get_child_element(xpath)
        list_items = list_element.find_elements(By.XPATH, "./li")
        return [
            Item(item.get_attribute("id"), item.get_attribute("innerText"))
            for item in list_items
        ]

    def is_visible(self, xpath: str) -> bool:
        element = self._get_child_element(xpath)
        return element.is_displayed()

    def select_list_item(
        self, xpath: str, label: str | None = None, id: str | None = None
    ):
        list_element = self._get_child_element(xpath)
        list_items = list_element.find_elements(By.XPATH, "./li")
        actions = ActionChains(self.webdriver)

        if not (id or label):
            raise ValueError('You must provide at least "label" or "id"!')

        for item in list_items:
            if label and label == item.get_attribute("innerText"):
                actions.click(item)
                actions.perform()
                return

            if id and id == item.get_attribute("id"):
                actions.click(item)
                actions.perform()
                return

        raise ValueError("Item not found!")

    def submit(self, button_xpath: str | None = None):
        if not button_xpath:
            self.element.submit()
        else:
            button = get_element(self.element, button_xpath, self.visibility_timeout)
            button.click()
