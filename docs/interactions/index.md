Once you have a `Web` object, you are able to browse on the web. The `Web` class is a abstraction of main browser and user functions.

```python linenums="1"
# The current URL from the browser
web.url
'https://www.site.com/mypage'

# The domain from the current URL
web.domain
'www.site.com'

# The title from the current page
web.title
'My website'

# Navigate to an URL
web.browse('https://www.site.com/another_page')

# Refresh the current page
web.refresh()

# Check if an element is interactive on the screen
web.is_interactive('//*[@id="myElement"]')
False

# Get the from text content from an element
web.read('//*[@id="myElement"]')
'Any text'

```

You can also, manage the following items:

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