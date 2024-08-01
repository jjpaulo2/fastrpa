Interactions with `input` and `textarea` tags.

```python
# Gets the right element class for the xpath
>>> my_input = web.element('//*[id="myInput"]')
>>> type(my_input)
fastrpa.core.elements.InputElement

# Try to get an InputElement
>>> my_input = web.input('//*[id="myInput"]')
>>> type(my_input)
fastrpa.core.elements.InputElement

# Clear the element value
>>> my_input.clear()

# Fill the input box with some value
>>> my_input.fill('my input')

# Fill the input box, key by key
>>> my_input.fill_slowly('my input')

# Fill the input box, key by key, waiting 3 seconds between every key send
>>> my_input.fill_slowly('my input', 3)
```