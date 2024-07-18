from typing import Type
from selenium.webdriver import (
    ChromeOptions,
    SafariOptions,
    FirefoxOptions,
    Chrome,
    Safari,
    Firefox,
    Remote,
)


WebDriver = Remote | Chrome | Safari | Firefox
BrowserOptions = ChromeOptions | SafariOptions | FirefoxOptions
BrowserOptionsClass = Type[ChromeOptions] | Type[SafariOptions] | Type[FirefoxOptions]


__all__ = (
    'WebDriver',
    'BrowserOptions',
    'BrowserOptionsClass',
)
