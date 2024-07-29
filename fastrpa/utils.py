from typing import Callable, Iterable
from urllib.parse import urlparse
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import StaleElementReferenceException
from rich.table import Table
from rich.console import Console

import os
import requests
import mimetypes

from fastrpa.types import BrowserOptions, BrowserOptionsClass, WebDriver


def get_browser_options(
    options: list[str], options_class: BrowserOptionsClass = ChromeOptions
) -> BrowserOptions:
    instance = options_class()
    for opt in options:
        instance.add_argument(opt)
    return instance


def get_file_path(path: str) -> str:
    if os.path.isfile(path):
        return path

    file_response = requests.get(path)
    file_extension = mimetypes.guess_extension(
        file_response.headers['Content-Type']
    )
    file_hash = abs(hash(file_response.content))
    download_path = f'/tmp/{file_hash}{file_extension}'

    with open(download_path, 'wb') as file:
        file.write(file_response.content)

    return download_path


def get_domain(webdriver: WebDriver) -> str:
    return urlparse(webdriver.current_url).netloc


def print_table(headers: Iterable[str], rows: Iterable[str]):
    rich_table = Table(*headers)
    for row in rows:
        rich_table.add_row(*row)
    Console().print(rich_table)


def ensure_element(func: Callable, max_attempts: int = 3):
    def wrapper(*args, **kwargs):
        attempt = 0
        while attempt < max_attempts:
            try:
                return func(*args, **kwargs)
            except StaleElementReferenceException:
                attempt += 1

    return wrapper
