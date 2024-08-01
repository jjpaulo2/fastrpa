Interactions with `button` and `a` tags.

```python
# Gets the right element class for the xpath
>>> my_button = web.element('//*[id="myButton"]')
>>> type(my_select)
fastrpa.core.elements.ButtonElement

# Try to get a ButtonElement
>>> my_button = web.button('//*[id="myButton"]')
>>> type(my_select)
fastrpa.core.elements.ButtonElement

# Check if the button is a link
>>> my_button.is_link
True

# Get the link reference
>>> my_button.reference
'https://www.mysite.com/page'

# Click in the button
>>> my_button.click()

# Perform a double click in the button
>>> my_button.double_click()
```