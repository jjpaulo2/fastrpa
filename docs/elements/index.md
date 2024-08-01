
> FastRPA is totally based on **xpath locations**. It means that does not exists any way, but xpath, to access elements from the web pages. This is a important concept that guarants the consistence on framework's code base. 
> 
> If you want to obtain elements using another identifier, just write an xpath that wraps that identifier. For example, if you want to get a div with an id `my_div`, just use the xpath `//*[@id="my_div"]`. You can use a site like [xpather.com](http://xpather.com/) to help you building your xpaths.

To start our interactions with page elements, we just need to obtain these with the methods shown below.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# To get just one element, or the first found
>>> web.element('//*[@id="my_div"]')
<fastrpa.core.elements.Element at 0x...>

# To get all elements found
>>> web.elements('//*[@id="my_div"]')
[<fastrpa.core.elements.Element at 0x...>,
 <fastrpa.core.elements.Element at 0x...>]
```

By default, FastRPA always waits until the element is interactable. The default timeout is 15 seconds, and it is configurable by the FastRPA constructor. In case of timeout, you will receive a `ElementTimeoutException`.

```python
>>> app = FastRPA(timeout=60)
>>> web = app.browse('https:...')

# If after the timeout, the element isn't avaliable
>>> web.elements('//*[@id="my_div"]')
Traceback (most recent call last):
    ...
ElementTimeoutException: Element [//*[@id="my_div"]] not found after 60 seconds!
```

If you don't want to wait, just send a wait=False parameter to the element method.

```python
>>> app = FastRPA(timeout=60)
>>> web = app.browse('https:...')

# Get an element without waiting
>>> web.elements('//*[@id="my_div"]', wait=False)
<fastrpa.core.elements.Element at 0x...>

# Try to get a element that is not on the page
>>> web.elements('//*[@id="my_div"]', wait=False)
ElementNotFoundException: No one element [//*[@id="my_div"]] was found!
```

There is some abstractions that implements actions and rules for specific elements. They is listed below.

- `Element`, for any element
- [`InputElement`](#inputs), for fillable inputs (`input`)
- [`FileInputElement`](#file-inputs), for file inputs (`input type="file"`)
- [`SelectElement`](#selects), for selects (`select`)
- [`ListElement`](#lists), for ordered and unordered lists (`ol`, `ul`)
- [`ButtonElement`](#buttons-and-links), for buttons and links (`button`, `a`)
- [`FormElement`](#forms), for forms (`form`)
- [`TableElement`](#tables), for tables (`table`)
- [`ImageElement`](#images), for any media like images and videos (`img`)

To interact with generical `Element` instances, you can use the properties and methods below.

```python
>>> element = web.element('//*[id="myElement"]')
>>> type(element)
fastrpa.core.elements.Element

# Get the element's tag
>>> element.tag
'div'

# Get the element's id
>>> element.id
'searchform'

# Get the element's class
>>> element.css_class
['form', 'form-styled']

# Get the element's inline css
>>> element.css_inline
{'background-image': 'url("...")'}

# Get the element's innerText or value
>>> element.text
'Fazer login'

# Returns if the element is visible for the user
>>> element.is_visible
True

# Returns the value for any element attribute, or None if doesn't exists
>>> element.attribute('data-property')
'any value'

# Check if some attribute has some value
>>> element.check('attribute', 'value')
False

# Scroll and move the cursor to the element
>>> element.focus()
```