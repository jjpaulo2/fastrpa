from typing import Type
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import (
    ActionChains,
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
    'ActionChains',
    'WebDriver',
    'WebElement',
    'Keys',
    'BrowserOptions',
    'BrowserOptionsClass',
)
