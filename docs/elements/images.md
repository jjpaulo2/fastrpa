Interactions with `img` tag.

## Reading the element

### Getting the right element class for the xpath

```python
>>> my_image = web.element('//*[id="myImage"]')
>>> type(my_select)
fastrpa.core.elements.ImageElement
```

### Try to get a `ImageElement`

```python
>>> my_image = web.image('//*[id="myImage"]')
>>> type(my_select)
fastrpa.core.elements.ImageElement
```

## Reference

### Get the image path from src attribute

```python
>>> my_image.reference
'https://mysite.com/resources/image.png'
```

### Get the alternative text from alt attribute

```python
>>> my_image.text
'An website image'
```

### Save the image on the current workdir

```python
>>> my_image.save()
```

### Save the image on a custom path

```python
>>> my_image.save('/my/path/image.png')
```
