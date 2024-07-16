from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

import os
import requests
import mimetypes

from fastrpa.settings import HIDDEN_TIMEOUT
from fastrpa.types import BrowserOptions, BrowserOptionsClass, WebDriver


def get_browser_options(
    options: list[str], options_class: BrowserOptionsClass = ChromeOptions
) -> BrowserOptions:
    instance = options_class()
    for opt in options:
        instance.add_argument(opt)
    return instance


def wait_until_element_is_hidden(
    webdriver_or_parent_node: WebDriver | WebElement,
    xpath: str,
    timeout: int = HIDDEN_TIMEOUT,
):
    WebDriverWait(webdriver_or_parent_node, timeout).until_not(
        expected_conditions.element_to_be_clickable((By.XPATH, xpath))
    )


def wait_until_element_is_present(
    webdriver_or_parent_node: WebDriver | WebElement,
    xpath: str,
    timeout: int = HIDDEN_TIMEOUT,
):
    WebDriverWait(webdriver_or_parent_node, timeout).until(
        expected_conditions.presence_of_element_located((By.XPATH, xpath))
    )


def get_file_path(path: str) -> str:
    if os.path.isfile(path):
        return path

    file_response = requests.get(path)
    file_extension = mimetypes.guess_extension(file_response.headers["Content-Type"])
    file_hash = abs(hash(file_response.content))
    download_path = f"/tmp/{file_hash}{file_extension}"

    with open(download_path, "wb") as file:
        file.write(file_response.content)

    return download_path
