from typing import Any
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from fastrpa.exceptions import KeyDoesNotExists
from fastrpa.types import WebDriver


class Keyboard:
    def __init__(self, webdriver: WebDriver):
        self._keys_mapping: dict[str, str] | None = None
        self._keys: list[str] | None = None
        self.webdriver = webdriver
        self.actions = ActionChains(self.webdriver)

    @property
    def keys_mapping(self) -> dict[str, str]:
        if self._keys_mapping is None:
            self._keys_mapping = {
                attr: getattr(Keys, attr)
                for attr in dir(Keys)
                if not attr.startswith('_')
            }
        return self._keys_mapping

    @property
    def keys(self) -> list[str]:
        if self._keys is None:
            self._keys = list(self.keys_mapping.keys())
        return self._keys

    def key_name(self, name: str) -> str:
        return name.upper().replace(' ', '_')

    def has_key(self, name: str | None = None, code: str | None = None) -> bool:
        if name:
            return self.key_name(name) in self.keys
        elif code:
            return code in self.keys_mapping.values()
        raise ValueError('You must provide at least "name" or "code"!')

    def key_code(self, key: str) -> str:
        key_name = self.key_name(key)
        if key_name in self.keys:
            return self.keys_mapping[key_name]
        elif key in self.keys_mapping.values():
            return key
        elif len(key) == 1:
            return key
        raise KeyDoesNotExists(key)

    def press(self, key: str):
        self.actions.send_keys(self.key_code(key))
        self.actions.perform()

    def shortcut(self, *keys: str):
        for key in keys:
            self.actions.key_down(self.key_code(key))
        for key in keys[::-1]:
            self.actions.key_up(self.key_code(key))
        self.actions.perform()

    def __contains__(self, value: Any) -> bool:
        return self.has_key(value) or self.has_key(code=value)
