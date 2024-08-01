# Interactions

You can manage easier the following items:

- [`keyboard`](./keyboard.md), to send key pressing events on the current page
- [`wait`](./wait.md), to wait for some events on the current page
- [`cookies`](./cookies.md), to manage cookies on the current page
- [`screenshot`](./screenshot.md), to download screenshots and prints from the current page
- [`tabs`](./tabs.md), to manage and navigate through the current opened tabs
- [`console`](./console.md), to run javascript on the current page

You can access these abstractions by calling it from the `Web` object.

```python linenums="1"
web.keyboard
<fastrpa.core.keyboard.Keyboard at 0x...>

web.wait
<fastrpa.core.wait.Wait at 0x...>

web.cookies
<fastrpa.core.cookies.Cookies at 0x...>

web.screenshot
<fastrpa.core.screenshot.Screenshot at 0x...>

web.tabs
<fastrpa.core.tabs.Tabs at 0x...>

web.console
<fastrpa.core.console.Console at 0x...>
```
