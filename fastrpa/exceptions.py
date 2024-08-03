class ElementNotFoundException(Exception):
    message = 'No one element [{}] was found!'

    def __init__(self, xpath: str):
        self.xpath = xpath
        super().__init__(self.message.format(xpath))


class ElementTimeoutException(Exception):
    message = 'Element [{}] not found after {} seconds!'

    def __init__(self, xpath: str, timeout: float):
        self.xpath = xpath
        self.timeout = timeout
        super().__init__(self.message.format(xpath, timeout))


class ElementNotCompatibleException(Exception):
    message = 'Element [{}] is not compatible with {}!'

    def __init__(self, xpath: str, class_name: type):
        self.xpath = xpath
        self.class_name = class_name
        super().__init__(self.message.format(xpath, class_name))


class ScreenshotNotTakenException(Exception):
    message = 'The [{}] screenshot from [{}] was not taken!'

    def __init__(self, type: str, url: str):
        self.type = type
        self.url = url
        super().__init__(self.message.format(type, url))


class CookieNotAddedException(Exception):
    message = 'The cookie [{}] was not added!'

    def __init__(self, cookie_name: str):
        self.cookie_name = cookie_name
        super().__init__(self.message.format(cookie_name))


class KeyDoesNotExistsException(Exception):
    message = 'The key [{}] does not exists!'

    def __init__(self, key: str):
        self.key = key
        super().__init__(self.message.format(key))


class FormException(Exception):
    message = (
        'The form submission got an error! Condition [{}, {}] not satisfied!'
    )

    def __init__(self, condition: str, expected_value: str):
        self.condition = condition
        self.expected_value = expected_value
        super().__init__(self.message.format(condition, expected_value))


class FileNotDownloadableException(Exception):
    message = 'The file [{}] at [{}] is not downloadable!'

    def __init__(self, url: str | None, xpath: str):
        self.url = url
        self.xpath = xpath
        super().__init__(self.message.format(url, xpath))
