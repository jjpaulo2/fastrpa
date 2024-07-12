from dataclasses import dataclass


@dataclass
class Option:
    value: str | None
    label: str | None


@dataclass
class Item:
    id: str | None
    label: str | None
