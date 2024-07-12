class ElementNotFound(Exception):
    message = "Element [{}] not found after {} seconds!"

    def __init__(self, xpath: str, timeout: int) -> None:
        super().__init__(self.message.format(xpath, timeout))
