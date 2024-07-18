from selenium.webdriver import ChromeOptions

import os
import requests
import mimetypes

from fastrpa.types import BrowserOptions, BrowserOptionsClass


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
    file_extension = mimetypes.guess_extension(file_response.headers['Content-Type'])
    file_hash = abs(hash(file_response.content))
    download_path = f'/tmp/{file_hash}{file_extension}'

    with open(download_path, 'wb') as file:
        file.write(file_response.content)

    return download_path
