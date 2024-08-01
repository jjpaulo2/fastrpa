Interactions with `input` with attribute `type="file"`.

## Reading the element

### Getting the right element class for the xpath

```python
>>> my_input = web.element('//*[id="myFileInput"]')
>>> type(my_input)
fastrpa.core.elements.FileInputElement
```

### Try to get a `FileInputElement`

```python
>>> my_input = web.file_input('//*[id="myFileInput"]')
>>> type(my_input)
fastrpa.core.elements.FileInputElement
```

## Reference

### Attach a local file

```python
>>> my_input.attach_file('/home/user/picture.png')
```

### Attach a file from the web

```python
>>> my_input.attach_file('https://website.com/picture.png')
```