---
description: Interactions with <input> tag with attribute [@type="file"].
---

Interactions with `input` with attribute `type="file"`.

## Reading the element

### Getting the right element class for the xpath

```python linenums="1"
my_input = web.element('//*[id="myFileInput"]')
type(my_input)
```

```python title="Output"
fastrpa.core.elements.FileInputElement
```

### Try to get a `FileInputElement`

```python linenums="1"
my_input = web.file_input('//*[id="myFileInput"]')
type(my_input)
```

```python title="Output"
fastrpa.core.elements.FileInputElement
```

## Reference

### Attach a local file

```python linenums="1"
my_input.attach_file('/home/user/picture.png')
```

### Attach a file from the web

```python linenums="1"
my_input.attach_file('https://website.com/picture.png')
```