from typing import Callable
from selenium.common.exceptions import StaleElementReferenceException


def ensure_element(func: Callable, max_attempts: int = 3):
    def wrapper(*args, **kwargs):
        attempt = 0
        while attempt < max_attempts:
            try:
                return func(*args, **kwargs)
            except StaleElementReferenceException:
                attempt += 1

    return wrapper
