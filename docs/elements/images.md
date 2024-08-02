---
description: Interactions with <img> tag.
---

Interactions with `img` tag.

## Reading the element

### Getting the right element class for the xpath

```python linenums="1"
my_image = web.element('//*[id="myImage"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.ImageElement
```

### Try to get a `ImageElement`

```python linenums="1"
my_image = web.image('//*[id="myImage"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.ImageElement
```

## Reference

### Get the image path from src attribute

```python linenums="1"
my_image.reference
```

```python title="Output"
'https://mysite.com/resources/image.png'
```

### Get the alternative text from alt attribute

```python linenums="1"
my_image.text
```

```python title="Output"
'An website image'
```

### Save the image on the current workdir

```python linenums="1"
my_image.save()
```

### Save the image on a custom path

```python linenums="1"
my_image.save('/my/path/image.png')
```
