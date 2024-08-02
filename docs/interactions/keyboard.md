---
description: Learn how to easily send keyboard events to the current page.
---

You can send keyboard events to the current page, by using the methods below.

## Accessing the object

```python linenums="1"
app = FastRPA()
web = app.browse('https:...')
type(web.keyboard)
```

```python title="Output"
fastrpa.core.keyboard.Keyboard
```

## Reference

!!! info 
    All keyboard methods are case insensitive.

### Get the available command keys

```python linenums="1"
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

### Simple key press event

```python linenums="1"
web.keyboad.press('control')
web.keyboad.press('escape')
web.keyboad.press('enter')
```

### Keyboard shortcut event

```python linenums="1"
web.keyboad.shortcut('control', 'a')
web.keyboad.shortcut('control', 'shift', 'c')
```