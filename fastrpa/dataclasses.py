from dataclasses import dataclass
from typing import Any, Literal


@dataclass
class Option:
    value: str | None
    label: str | None


@dataclass
class Item:
    id: str | None
    label: str | None


@dataclass
class Cookie:
    name: str
    value: str
    domain: str
    path: str = '/'
    secure: bool = False
    http_only: bool = True
    same_site: Literal["Strict", "Lax", "None"] = "None"

    @staticmethod
    def from_selenium(content: dict[str, Any]) -> 'Cookie':
        return Cookie(
            name=content['name'],
            value=content['value'],
            domain=content['domain'],
            path=content['path'],
            secure=content['secure'],
            http_only=content['httpOnly'],
            same_site=content['sameSite'],
        )
    
    def to_selenium(self) -> dict[str, Any]:
        return {
            'name': self.name,
            'value': self.value,
            'domain': self.domain,
            'path': self.path,
            'secure': self.secure,
            'httpOnly': self.http_only,
            'sameSite': self.same_site,
        }
