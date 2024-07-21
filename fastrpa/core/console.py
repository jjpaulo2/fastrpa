from typing import Any
from fastrpa.types import WebDriver


class Console:

    def __init__(self, webdriver: WebDriver) -> None:
        self.webdriver = webdriver

    def evaluate(self, code: str) -> Any:
        return self.webdriver.execute_script(f'return {code}')

    def run(self, lines: list[str]) -> Any:
        return self.webdriver.execute_script('\n'.join(lines))
    
    def run_script(self, path: str) -> Any:
        with open(path, 'r') as script:
            return self.run(script.readlines())
