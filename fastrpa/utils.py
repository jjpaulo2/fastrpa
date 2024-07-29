from typing import Callable, Iterable
from urllib.parse import urlparse
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from requests import Session

from fastrpa.types import BrowserOptions, BrowserOptionsClass, WebDriver


def get_browser_options(
    options: list[str], options_class: BrowserOptionsClass = ChromeOptions
) -> BrowserOptions:
    instance = options_class()
    for opt in options:
        instance.add_argument(opt)
    return instance


def get_session(webdriver: WebDriver) -> Session:
    obj = Session()
    for cookie in webdriver.get_cookies():
        obj.cookies.set(
            name=cookie['name'],
            value=cookie['value'],
            domain=cookie['domain'],
            path=cookie['path'],
            secure=cookie['secure'],
        )
    return obj


def get_domain(webdriver: WebDriver) -> str:
    return urlparse(webdriver.current_url).netloc


def find_element(browsable: WebDriver | WebElement, xpath: str) -> WebElement:
    return browsable.find_element(By.XPATH, xpath)


def find_elements(
    browsable: WebDriver | WebElement, xpath: str
) -> list[WebElement]:
    return browsable.find_elements(By.XPATH, xpath)


def print_table(headers: Iterable[str], rows: Iterable[str]):
    try:
        from rich.table import Table
        from rich.console import Console

        rich_table = Table(*headers)
        for row in rows:
            rich_table.add_row(*row)
        Console().print(rich_table)

    except ImportError:
        raise EnvironmentError('You need to install rich to print tables.')


def print_list(name: str, values_dict: dict[str | None, str | None]):
    try:
        from rich.tree import Tree
        from rich.console import Console

        rich_tree = Tree(name.replace('[', '\['))
        for id, value in values_dict.items():
            rich_tree.add(f'[{id}] {value}')
        Console().print(rich_tree)

    except ImportError:
        raise EnvironmentError('You need to install rich to print lists.')


def ensure_element(func: Callable, max_attempts: int = 3):
    def wrapper(*args, **kwargs):
        attempt = 0
        while attempt < max_attempts:
            try:
                return func(*args, **kwargs)
            except StaleElementReferenceException:
                attempt += 1

    return wrapper
