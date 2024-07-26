from time import sleep
from typing import Any
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from fastrpa.commons import get_file_path, print_table
from fastrpa.dataclasses import Item, Option
from fastrpa.types import WebDriver


class Element:
    _tag: str | None = None
    _id: str | None = None

    def __init__(self, source: WebElement, webdriver: WebDriver) -> None:
        self.source = source
        self.webdriver = webdriver
        self.actions = ActionChains(self.webdriver)

    def attribute(self, name: str) -> str | None:
        return self.source.get_attribute(name)

    @property
    def tag(self) -> str:
        if self._tag is None:
            self._tag = self.source.tag_name
        return self._tag

    @property
    def id(self) -> str | None:
        if self._id is None:
            self._id = self.attribute('id')
        return self._id

    @property
    def css_class(self) -> list[str] | None:
        if classes := self.attribute('class'):
            return classes.split(' ')
        return []
    
    @property
    def css_inline(self) -> dict[str, str]:
        to_return = {}
        if style := self.attribute('style'):
            for css in style.strip().split(';'):
                if css:
                    css_property, css_value = css.split(':')
                    to_return[css_property.strip()] = css_value.strip()
        return to_return

    @property
    def text(self) -> str | None:
        if self.source.text:
            return self.source.text
        elif value := self.attribute('value'):
            return value
        return None

    @property
    def is_visible(self) -> bool:
        return self.source.is_displayed()

    def focus(self):
        self.actions.scroll_to_element(self.source)
        self.actions.move_to_element(self.source)
        self.actions.perform()

    def check(self, attribute: str, value: str) -> bool:
        return self.attribute(attribute) == value


class InputElement(Element):
    def clear(self):
        self.source.clear()

    def fill(self, value: str):
        self.source.send_keys(value)

    def fill_slowly(self, value: str, delay: float = 0.3):
        for key in value:
            self.source.send_keys(key)
            sleep(delay)


class FileInputElement(Element):
    def attach_file(self, path: str):
        self.source.send_keys(get_file_path(path))


class SelectElement(Element):
    _select_source: Select | None = None

    @property
    def select_source(self) -> Select:
        if not self._select_source:
            self._select_source = Select(self.source)
        return self._select_source

    @property
    def options_values(self) -> list[str | None]:
        return [
            option.get_attribute('value')
            for option in self.select_source.options
        ]

    @property
    def options_labels(self) -> list[str | None]:
        return [
            option.get_attribute('innerText')
            for option in self.select_source.options
        ]

    @property
    def options(self) -> list[Option]:
        return [
            Option(
                option.get_attribute('value'),
                option.get_attribute('innerText'),
            )
            for option in self.select_source.options
        ]

    def select(self, label: str | None = None, value: str | None = None):
        if label:
            self.select_source.select_by_visible_text(label)
        elif value:
            self.select_source.select_by_value(value)
        else:
            raise ValueError('You must provide at least "label" or "value"!')

    def has_option(self, label: str | None = None, value: str | None = None):
        if label:
            return label in self.options_labels
        elif value:
            return value in self.options_values
        raise ValueError('You must provide at least "label" or "value"!')

    def __contains__(self, key: Any) -> bool:
        return self.has_option(label=key) or self.has_option(value=key)


class ListElement(Element):
    _is_ordered: bool | None = None
    _items_sources: list[WebElement] | None = None

    @property
    def items_sources(self) -> list[WebElement]:
        if self._items_sources is None:
            self._items_sources = self.source.find_elements(By.XPATH, './/li')
        return self._items_sources

    @property
    def is_ordered(self) -> bool:
        if self._is_ordered is None:
            self._is_ordered = self.tag == 'ol'
        return self._is_ordered

    @property
    def items(self) -> list[Item]:
        return [
            Item(item.get_attribute('id'), item.get_attribute('innerText'))
            for item in self.items_sources
        ]

    @property
    def items_ids(self) -> list[str | None]:
        return [
            item.get_attribute('ids')
            for item in self.items_sources
        ]

    @property
    def items_labels(self) -> list[str | None]:
        return [
            item.get_attribute('innerText')
            for item in self.items_sources
        ]

    def click_in_item(self, label: str | None = None, id: str | None = None):
        if not (label or id):
            raise ValueError('You must provide at least "label" or "id"!')

        for item in self.items_sources:
            if label and label == item.get_attribute('innerText'):
                self.actions.click(item)
                self.actions.perform()
                return

            if id and id == item.get_attribute('id'):
                self.actions.click(item)
                self.actions.perform()
                return

        raise ValueError('Item not found!')

    def has_item(self, label: str | None = None, id: str | None = None):
        if label:
            return label in self.items_labels
        elif id:
            return id in self.items_ids
        raise ValueError('You must provide at least "label" or "id"!')

    def __contains__(self, key: Any) -> bool:
        return self.has_item(label=key) or self.has_item(id=key)


class ButtonElement(Element):
    _is_link: bool | None = None

    @property
    def is_link(self) -> bool:
        if self._is_link is None:
            self._is_link = (self.tag == 'a')
        return self._is_link

    @property
    def reference(self) -> str | None:
        if self.is_link:
            return self.attribute('href')
        return None

    def click(self):
        self.actions.move_to_element(self.source)
        self.actions.click(self.source)
        self.actions.perform()

    def double_click(self):
        self.actions.move_to_element(self.source)
        self.actions.double_click(self.source)
        self.actions.perform()


class FormElement(Element):
    def submit(self, button: ButtonElement | None = None):
        if not button:
            self.source.submit()
        else:
            button.click()


class TableElement(Element):
    _headers_sources: list[WebElement] | None = None
    _rows_sources: list[WebElement] | None = None

    @property
    def headers_sources(self) -> list[WebElement]:
        if self._headers_sources is None:
            first_row = self.source.find_element(By.XPATH, './/tr')
            self._headers_sources = first_row.find_elements(By.XPATH, './/th')
        return self._headers_sources

    @property
    def headers(self) -> list[str | None]:
        return [
            header.get_attribute('innerText') if header else None
            for header in self.headers_sources
        ]

    @property
    def rows_sources(self) -> list[WebElement]:
        if self._rows_sources is None:
            rows = self.source.find_elements(By.XPATH, './/tr')
            if self.headers:
                del rows[0]
            self._rows_sources = rows
        return self._rows_sources

    @property
    def rows(self) -> list[list[str | None]]:
        rows_content = []
        for element in self.rows_sources:
            rows_content.append(
                [
                    cell.get_attribute('innerText')
                    for cell in element.find_elements(
                        By.XPATH, './/td | .//th'
                    )
                ]
            )
        return rows_content

    def column_values(
        self, name: str | None = None, index: int | None = None
    ) -> list[str | None]:
        if (not name) and (index is None):
            raise ValueError('You must provide at least "name" or "index"!')

        if index is None:
            index = self.headers.index(name)

        return [row[index] for row in self.rows]

    def has_content(self, value: str) -> bool:
        cells_content = [
            cell.get_attribute('innerText')
            for cell in self.source.find_elements('.//td')
        ]
        return value in cells_content
    
    def __contains__(self, value: Any) -> bool:
        return self.has_content(value)

    def print(self):
        print_table(self.headers, self.rows)
