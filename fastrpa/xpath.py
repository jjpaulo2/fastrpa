def id_contains(value: str, child: str = '') -> str:
    return f'//*[contains(@id, "{value}")]{child}'


def class_contains(value: str, child: str = '') -> str:
    return f'//*[contains(@class, "{value}")]{child}'


def name_contains(value: str, child: str = '') -> str:
    return f'//*[contains(@name, "{value}")]{child}'


def text_contains(value: str, child: str = '') -> str:
    return f'//*[contains(text(), "{value}")]{child}'
