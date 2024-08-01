Interactions with `input` with attribute `type="file"`.

```python
# Gets the right element class for the xpath
>>> my_input = web.element('//*[id="myFileInput"]')
>>> type(my_input)
fastrpa.core.elements.FileInputElement

# Try to get a FileInputElement
>>> my_input = web.file_input('//*[id="myFileInput"]')
>>> type(my_input)
fastrpa.core.elements.FileInputElement

# Attach a local file
>>> my_input.attach_file('/home/user/picture.png')

# Attach a file from the web
>>> my_input.attach_file('https://website.com/picture.png')
```