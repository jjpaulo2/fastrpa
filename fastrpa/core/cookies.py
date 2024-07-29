from typing import Any

from fastrpa.utils import get_domain
from fastrpa.exceptions import CookieNotAdded
from fastrpa.types import WebDriver, Cookie


class Cookies:
    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    @property
    def list_names(self) -> list[str]:
        cookies = []
        for cookie in self.webdriver.get_cookies():
            cookies.append(cookie['name'])
        return cookies

    @property
    def list(self) -> list[Cookie]:
        cookies = []
        for cookie in self.webdriver.get_cookies():
            cookies.append(Cookie.from_selenium(cookie))
        return cookies

    def get(self, name: str) -> Cookie | None:
        if cookie := self.webdriver.get_cookie(name):
            return Cookie.from_selenium(cookie)
        return None

    def add(self, name: str, value: str, secure: bool = False) -> Cookie:
        domain = get_domain(self.webdriver)
        cookie = Cookie(name, value, domain, secure=secure)
        self.webdriver.add_cookie(cookie.to_selenium())
        if added_cookie := self.webdriver.get_cookie(name):
            return Cookie.from_selenium(added_cookie)
        raise CookieNotAdded(name)

    def delete(self, name: str):
        self.webdriver.delete_cookie(name)

    def check(self, name: str, value: str) -> bool:
        if cookie := self.get(name):
            return cookie.value == value
        return False

    def has_cookie(self, name: str) -> bool:
        return name in self.list_names

    def __contains__(self, key: Any) -> bool:
        return key in self.list_names
