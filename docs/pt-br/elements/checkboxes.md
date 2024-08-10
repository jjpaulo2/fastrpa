---
description: Interactions with input tag with attribute [@type="checkbox"].
---

Interactions with `input` with attribute `type="checkbox"`.

## Reading the element

### Getting the right element class for the xpath

```python linenums="1"
my_check = web.checkbox('//*[id="myCheckbox"]')
type(my_check)
```

```python title="Output"
fastrpa.core.elements.CheckboxElement
```

### Try to get a `CheckboxElement`

```python linenums="1"
my_check = web.checkbox('//*[id="myCheckbox"]')
type(my_check)
```

```python title="Output"
fastrpa.core.elements.CheckboxElement
```

## Reference

### Get if it's checked

```python linenums="1"
my_check.is_checked
```

```python title="Output"
False
```

### Set as checked

Only set the checkbox as checked/active.

```python linenums="1"
my_radio.check()
```

### Set as unchecked

Only set the checkbox as unchecked/inactive.

```python linenums="1"
my_radio.uncheck()
```

### Switch the value

Just switch the checkbox value. If it's checked, it will be unchecked, and vice versa.

```python linenums="1"
my_radio.switch()
```
