You can send keyboard events to the current page, by using the methods below.

```python linenums="1"
app = FastRPA()
web = app.browse('https:...')

# To send a simple key press event
web.keyboad.press('control')
web.keyboad.press('escape')
web.keyboad.press('enter')

# To send a keyboard shortcut event
web.keyboad.shortcut('control', 'a')
web.keyboad.shortcut('control', 'shift', 'c')

# To see the available command keyboard keys
web.keyboad.keys
['ADD',
 'ALT',
 'ARROW_DOWN',
 'ARROW_LEFT',
 'ARROW_RIGHT',
 'ARROW_UP',
 'BACKSPACE',
 'BACK_SPACE',
 ...
```