Interactions with `button` and `a` tags.

## Reading the element

### Getting the right element class for the xpath

```python
>>> my_button = web.element('//*[id="myButton"]')
>>> type(my_select)
fastrpa.core.elements.ButtonElement
```

### Try to get a `ButtonElement`

```python
>>> my_button = web.button('//*[id="myButton"]')
>>> type(my_select)
fastrpa.core.elements.ButtonElement
```

## Reference

### Check if the button is a link

```python
>>> my_button.is_link
True
```

### Get the link reference

```python
>>> my_button.reference
'https://www.mysite.com/page'
```

### Perform a double click in the button

```python
>>> my_button.double_click()
```
