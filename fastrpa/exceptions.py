class ElementNotFound(Exception):
    message = 'Element [{}] not found!'

    def __init__(self, xpath: str) -> None:
        super().__init__(self.message.format(xpath))


class ElementNotFoundAfterTime(Exception):
    message = 'Element [{}] not found after {} seconds!'

    def __init__(self, xpath: str, timeout: int) -> None:
        super().__init__(self.message.format(xpath, timeout))


class ElementNotCompatible(Exception):
    message = 'Element [{}] is not compatible with {}!'

    def __init__(self, xpath: str, class_name: type) -> None:
        super().__init__(self.message.format(xpath, class_name))


class CookieNotAdded(Exception):
    message = 'The cookie [{}] was not added!'

    def __init__(self, cookie_name: str) -> None:
        super().__init__(self.message.format(cookie_name))
