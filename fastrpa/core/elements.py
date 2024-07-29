from time import sleep
from typing import Any
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

from fastrpa.core.file import File
from fastrpa.exceptions import FileNotDownloadableException, FormException
from fastrpa.utils import (
    find_element,
    find_elements,
    print_list,
    print_table,
)
from fastrpa.types import WebDriver


class Element:
    def __init__(self, xpath: str, webdriver: WebDriver) -> None:
        self.xpath = xpath
        self.webdriver = webdriver
        self.file = File(self.webdriver)
        self.actions = ActionChains(self.webdriver)

    @property
    def source(self) -> WebElement:
        return find_element(self.webdriver, self.xpath)

    def attribute(self, name: str) -> str | None:
        return self.source.get_attribute(name)

    @property
    def tag(self) -> str:
        return self.source.tag_name

    @property
    def id(self) -> str | None:
        return self.attribute('id')

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

    def click(self):
        self.focus()
        self.actions.click(self.source)
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
        self.source.send_keys(self.file.get_path(path))


class SelectElement(Element):
    @property
    def select_source(self) -> Select:
        return Select(self.source)

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
    def options(self) -> dict[str | None, str | None]:
        return {
            option.get_attribute('value'): option.get_attribute('innerText')
            for option in self.select_source.options
        }

    @property
    def current(self) -> tuple[str | None, str | None]:
        if value_id := self.attribute('value'):
            return value_id, self.options[value_id]
        return None, None

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

    def print(self):
        identifier = f'[@id="{self.id}"]' if self.id else self.xpath
        print_list(f'{identifier}', self.options)


class ListElement(Element):
    @property
    def items_sources(self) -> list[WebElement]:
        return find_elements(self.webdriver, './/li')

    @property
    def is_ordered(self) -> bool:
        return self.tag == 'ol'

    @property
    def items(self) -> dict[str | None, str | None]:
        return {
            item.get_attribute('id'): item.get_attribute('innerText')
            for item in self.items_sources
        }

    @property
    def items_ids(self) -> list[str | None]:
        return [item.get_attribute('ids') for item in self.items_sources]

    @property
    def items_labels(self) -> list[str | None]:
        return [item.get_attribute('innerText') for item in self.items_sources]

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

    def print(self):
        identifier = f'[@id="{self.id}"]' if self.id else self.xpath
        print_list(identifier, self.items)


class ButtonElement(Element):
    @property
    def is_link(self) -> bool:
        return self.tag == 'a'

    @property
    def reference(self) -> str | None:
        if self.is_link:
            return self.attribute('href')
        return None

    def double_click(self):
        self.actions.move_to_element(self.source)
        self.actions.double_click(self.source)
        self.actions.perform()


class FormElement(Element):
    _success_redirect_url: str | None = None
    _success_elements_to_find: list[str] = []
    _success_text_to_find: list[str] = []

    def _check_success_conditions(self):
        if self._success_redirect_url is not None:
            if self.webdriver.current_url != self._success_redirect_url:
                raise FormException('redirect_url', self._success_redirect_url)

        for element in self._success_elements_to_find:
            try:
                find_element(self.webdriver, element)
            except NoSuchElementException:
                raise FormException('elements_to_find', element)

        for text in self._success_text_to_find:
            if text not in self.webdriver.page_source:
                raise FormException('text_to_find', text)

    @property
    def method(self) -> str:
        if gotten_method := self.attribute('method'):
            return gotten_method.upper()
        return 'GET'

    @property
    def action(self) -> str | None:
        return self.attribute('action')

    @property
    def type(self) -> str:
        if gotten_type := self.attribute('enctype'):
            return gotten_type
        return 'application/x-www-form-urlencoded'

    def set_success_condition(
        self,
        redirect_url: str | None = None,
        elements_to_find: list[str] = [],
        text_to_find: list[str] = [],
    ):
        self._success_redirect_url = redirect_url
        self._success_elements_to_find = elements_to_find
        self._success_text_to_find = text_to_find

    def submit(self, button_xpath: str | None = None):
        if not button_xpath:
            self.source.submit()
        else:
            button = ButtonElement(button_xpath, self.webdriver)
            button.click()
        self._check_success_conditions()


class TableElement(Element):
    @property
    def headers_sources(self) -> list[WebElement]:
        first_row = find_element(self.source, './/tr')
        return find_elements(first_row, './/th')

    @property
    def headers(self) -> list[str | None]:
        return [
            header.get_attribute('innerText') if header else None
            for header in self.headers_sources
        ]

    @property
    def rows_sources(self) -> list[WebElement]:
        rows = find_elements(self.source, './/tr')
        if self.headers:
            del rows[0]
        return rows

    @property
    def rows(self) -> list[list[str | None]]:
        rows_content = []
        for element in self.rows_sources:
            rows_content.append(
                [
                    cell.get_attribute('innerText')
                    for cell in find_elements(element, './/td | .//th')
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


class ImageElement(Element):
    @property
    def text(self) -> str | None:
        return self.attribute('alt')

    @property
    def reference(self) -> str | None:
        return self.attribute('src')

    def save(self, path: str | None = None):
        if not self.reference:
            raise FileNotDownloadableException(self.reference, self.xpath)
        if path is not None:
            self.file.download_file(self.reference, path)
        else:
            self.file.download_file_to_cwd(self.reference)
