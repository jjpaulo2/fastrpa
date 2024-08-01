Interactions with `input` and `textarea` tags.

## Reading the element

### Getting the right element class for the xpath

```python
>>> my_input = web.element('//*[id="myInput"]')
>>> type(my_input)
fastrpa.core.elements.InputElement
```

### Try to get an `InputElement`

```python
>>> my_input = web.input('//*[id="myInput"]')
>>> type(my_input)
fastrpa.core.elements.InputElement
```

## Reference

### Clear the element value

```python
>>> my_input.clear()
```

### Fill the input box with some value

```python
>>> my_input.fill('my input')
```

### Fill the input box, key by key

```python
>>> my_input.fill_slowly('my input')

# Fill the input box, key by key, waiting 3 seconds between every key send
>>> my_input.fill_slowly('my input', 3)
```