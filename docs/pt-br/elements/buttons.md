---
description: Interactions with button and a tags.
---

Interactions with `button` and `a` tags.

## Reading the element

### Getting the right element class for the xpath

```python linenums="1"
my_button = web.element('//*[id="myButton"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.ButtonElement
```

### Try to get a `ButtonElement`

```python linenums="1"
my_button = web.button('//*[id="myButton"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.ButtonElement
```

## Reference

### Check if the button is a link

```python linenums="1"
my_button.is_link
```

```python title="Output"
True
```

### Get the link reference

```python linenums="1"
my_button.reference
```

```python title="Output"
'https://www.mysite.com/page'
```

### Perform a double click in the button

```python linenums="1"
```

```python title="Output"
my_button.double_click()
```
