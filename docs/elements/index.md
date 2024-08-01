# Elements

> FastRPA is totally based on **xpath locations**. It means that does not exists any way, but xpath, to access elements from the web pages. This is a important concept that guarants the consistence on framework's code base. 
> 
> If you want to obtain elements using another identifier, just write an xpath that wraps that identifier. For example, if you want to get a div with an id `my_div`, just use the xpath `//*[@id="my_div"]`. You can use a site like [xpather.com](http://xpather.com/) to help you building your xpaths.

## Get elements from the page

To start our interactions with page elements, we just need to obtain these with the methods shown below.

### Get just one element or the first found

```python
>>> web.element('//*[@id="my_div"]')
<fastrpa.core.elements.Element at 0x...>
```

#### The wait strategy

By default, FastRPA always waits until the element is interactable. The default timeout is 15 seconds, and it is configurable by the FastRPA constructor. In case of timeout, you will receive a `ElementTimeoutException`.

```python
>>> app = FastRPA(timeout=60)
>>> web = app.browse('https:...')

# If after the timeout, the element isn't avaliable
>>> web.element('//*[@id="my_div"]')
Traceback (most recent call last):
    ...
ElementTimeoutException: Element [//*[@id="my_div"]] not found after 60 seconds!
```

#### Disabling the waiting

If you don't want to wait, just send a `wait=False` parameter to the element method.

```python
>>> app = FastRPA(timeout=60)
>>> web = app.browse('https:...')

# Get an element without waiting
>>> web.elements('//*[@id="my_div"]', wait=False)
<fastrpa.core.elements.Element at 0x...>

# Try to get a element that is not on the page
>>> web.elements('//*[@id="my_div"]', wait=False)
Traceback (most recent call last):
    ...
ElementNotFoundException: No one element [//*[@id="my_div"]] was found!
```

### Get all elements found

```python
>>> web.elements('//*[@id="my_div"]')
[<fastrpa.core.elements.Element at 0x...>,
 <fastrpa.core.elements.Element at 0x...>]
```

In the case of trying to get many elements, the framework will now run a wait strategy.

```python
>>> web.elements('//*[@id="my_inexistent_div"]')
Traceback (most recent call last):
    ...
ElementNotFoundException: No one element [//*[@id="my_div"]] was found!
```

## Elements abstractions

There is some abstractions that implements actions and rules for specific elements. They is listed below.

| Class | HTML5 tags |
|-|-|
| [`Element`](#element-reference) | any element |
| [`InputElement`](./inputs.md) | `input`, `textarea` |
| [`FileInputElement`](./file-inputs.md) | `input type="file"` |
| [`SelectElement`](./selects.md) | `select` |
| [`ListElement`](./lists.md) | `ol`, `ul` |
| [`ButtonElement`](./buttons.md) | `button`, `a` |
| [`FormElement`](./forms.md) | `form` |
| [`TableElement`](./tables.md) | `table` |
| [`ImageElement`](./images.md) | `img` |

## Element reference

To interact with generical `Element` instances, you can use the properties and methods below.

### Get the element

```python
>>> element = web.element('//*[id="myElement"]')
>>> type(element)
fastrpa.core.elements.Element
```

### Get the tag

```python
>>> element.tag
'div'
```

### Get the id

```python
>>> element.id
'searchform'
```

### Get the classes

```python
>>> element.css_class
['form', 'form-styled']
```

### Get the inline css

```python
>>> element.css_inline
{'background-image': 'url("...")'}
```

### Get the text or value

```python
>>> element.text
'Fazer login'
```

### Returns if the element is visible for the user

```python
>>> element.is_visible
True
```

### Returns the value for any element attribute, or None if doesn't exists

```python
>>> element.attribute('data-property')
'any value'
```

### Check if some attribute has some value

```python
>>> element.check('attribute', 'value')
False
```

### Scroll and move the cursor to the element

```python
>>> element.focus()
```