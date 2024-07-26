from typing import Any
from fastrpa.types import WebDriver


class Tabs:

    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver
    
    @property
    def list(self) -> list[str]:
        return self.webdriver.window_handles
    
    @property
    def current(self) -> str:
        return self.webdriver.current_window_handle
    
    @property
    def current_index(self) -> int:
        return self.list.index(self.current)

    @property
    def count(self) -> int:
        return len(self.list)
    
    def new(self) -> str:
        self.webdriver.switch_to.new_window('tab')
        return self.list[-1]

    def switch(self, tab: str | None = None, index: int | None = None):
        if tab:
            self.webdriver.switch_to.window(tab)
        elif index is not None:
            self.webdriver.switch_to.window(self.list[index])
        else:
            raise ValueError('You must provide at least "tab" or "index"!')

    def close(self):
        current_tab_index = self.current_index
        if self.count >= 2:
            self.webdriver.close()
            self.switch(index=current_tab_index-1)
        else:
            self.new()
            self.switch(index=current_tab_index)
            self.webdriver.close()
            self.switch(index=current_tab_index)

    def __len__(self) -> int:
        return self.count
    
    def __contains__(self, value: Any) -> bool:
        return value in self.list
    