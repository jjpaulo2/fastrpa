Interactions with `img` tag.

```python
# Gets the right element class for the xpath
>>> my_image = web.element('//*[id="myImage"]')
>>> type(my_select)
fastrpa.core.elements.ImageElement

# Try to get a ImageElement
>>> my_image = web.image('//*[id="myImage"]')
>>> type(my_select)
fastrpa.core.elements.ImageElement

# Get the image path from src attribute
>>> my_image.reference
'https://mysite.com/resources/image.png'

# Get the alternative text from alt attribute
>>> my_image.text
'An website image'

# Save the image on the current workdir
>>> my_image.save()

# Save the image on a custom path
>>> my_image.save('/my/path/image.png')
```
