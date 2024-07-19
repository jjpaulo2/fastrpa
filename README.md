# FastRPA

A simple to use abstraction over Selenium.

### Sumary

- [Configure Selenium integration](#configure-selenium-integration)
- [The FastRPA instance](#the-fastrpa-instance)
- [Interacting with the current page](#interacting-with-the-current-page)
    - [Pressing keys](#pressing-keys)
    - [Waiting for events](#waiting-for-events)
    - [Managing cookies](#managing-cookies)
    - [Take screenshots and prints](#take-screenshots-and-prints)
    - [Manage and navigate through opened tabs](#manage-and-navigate-through-opened-tabs)
    - [Running javascript](#running-javascript)
- [Interacting with the page elements](#interacting-with-the-page-elements)
    - [Inputs](#inputs)
    - [File inputs](#file-inputs)
    - [Selects](#selects)
    - [Lists](#lists)
    - [Buttons and links](#buttons-and-links)
    - [Tables](#tables)
    - [Medias](#medias)


## Configure Selenium integration

FastRPA needs a webdriver to work. It can be local, or remote. It's recommended to always use remote sessions.

You can run a remote session of Chromium webdriver using docker, as below.

```shell
# For x86 machines
docker run --name selenium -d -p 4444:4444 -p 7900:7900 selenium/standalone-chromium:latest

# For ARM machines
docker run --name selenium -d -p 4444:4444 -p 7900:7900 seleniarm/standalone-chromium:latest
```

By default, FastRPA always connect to `http://localhost:4444`. If you want to change it, just create your own Selenium instance.

```python
>>> from fastrpa import FastRPA
>>> from selenium.webdriver import Firefox, FirefoxOptions

>>> options = FirefoxOptions()
>>> options.add_argument(...)
>>> options.add_argument(...)

>>> webdriver = Firefox(options)
>>> app = FastRPA(webdriver)
```

## The FastRPA instance

This is just a configuration object. You will need it just to start your web navegation.

```python
>>> from fastrpa import FastRPA
>>> app = FastRPA()
>>> web = app.browse('https:...')
>>> type(web)
fastrpa.app.Web
```

## Interacting with the current page

Once you have a `Web` object, you are able to browse on the web. The `Web` class is a abstraction of main browser and user functions.

It includes, managing:

- [`keyboard`](#pressing-keys), to send key pressing events on the current page
- [`timer`](#waiting-for-events), to wait for some events on the current page
- [`cookies`](#managing-cookies), to manage cookies on the current page
- [`screenshot`](#take-screenshots-and-prints), to download screenshots and prints from the current page
- [`tabs`](#manage-and-navigate-through-opened-tabs), to manage and navigate through the current opened tabs
- [`console`](#running-javascript), to run javascript on the current page

You can access these abstractions by calling it from the `Web` object.

```python
>>> web.keyboard
<fastrpa.core.keyboard.Keyboard at 0x...>

>>> web.timer
<fastrpa.core.timer.Timer at 0x...>

>>> web.cookies
<fastrpa.core.cookies.Cookies at 0x...>

>>> web.screenshot
<fastrpa.core.screenshot.Screenshot at 0x...>

>>> web.tabs
<fastrpa.core.tabs.Tabs at 0x...>

>>> web.console
<fastrpa.core.console.Console at 0x...>
```

### Pressing keys

You can send simple pressing key events to the current page, by using the methods below.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# You can press the following keys
>>> web.keyboad.esc()
>>> web.keyboad.tab()
>>> web.keyboad.enter()
>>> web.keyboad.backspace()
>>> web.keyboad.home()
>>> web.keyboad.page_up()
>>> web.keyboad.page_down()
```

### Waiting for events

You can wait some time before or after execute some action with the automation. The method is just a simple proxy for `time.sleep`, to remove the need of more one import.

You can also wait for element visibility. By default the timeout is 15 seconds, but you can also specify it.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# Runs a time.sleep(15)
>>> web.timer.wait_seconds(10)

# Wait a maximum of 15 seconds until a button is present
>>> web.timer.wait_until_present('//button[@id="myBtn"]')

# Wait a maximum of custom seconds until a button is present
>>> web.timer.wait_until_present('//button[@id="myBtn"]', 30)

# Wait a maximum of 15 seconds until a button is hide
>>> web.timer.wait_until_hide('//button[@id="myBtn"]')

# Wait a maximum of custom seconds until a button is hide
>>> web.timer.wait_until_hide('//button[@id="myBtn"]', 30)
```

### Managing cookies

An abstraction to manage cookies on the current domain.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# Get the list of cookies on the current domain
>>> web.cookies.list
[Cookie(...), Cookie(...)]

# Get the list of names from the cookies on the current domain
>>> web.cookies.list_names
['JSESSIONID', '_ga', ...]

# Check if a cookie exists on the current domain
>>> 'my_cookie' in web.cookies
True

# Check if a cookie stores some value
>>> web.cookies.check('my_cookie', 'value')
False

# Get a cookie on the current domain
>>> web.cookies.get('my_cookie')
Cookie(name='...', value='...', domain='...', path='/', secure=True, http_only=True, same_site='Strict')

# Try to get a cookie that does not exist the current domain
>>> web.cookies.get('my_cookie')
None

# Add a new cookie on the current domain
>>> web.cookies.add('my_cookie', 'value', secure=False)
Cookie(name='my_cookie', value='value', domain='...', path='/', secure=False, http_only=True, same_site='Strict')
```

### Take screenshots and prints

By default, all screenshot methods save the files in the current active directory.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# Take a screenshot just containing the current viewport size
>>> web.screenshot.viewport()

# Take a screenshot just containing the current viewport size, and save the file in the specified path
>>> web.screenshot.viewport('/my/screenshot/path.png')

# Take a screenshot containing the complete page
>>> web.screenshot.full_page()

# Take a screenshot containing the complete page, and save the file in the specified path
>>> web.screenshot.full_page('/my/screenshot/path.png')
```

You can see examples of both screenshot methods below.

| Viewport screenshot | Full page screenshot |
|-|-|
| ![image](https://github.com/user-attachments/assets/ec5abfe0-5858-450a-a938-9fff58f89b86) | ![image](https://github.com/user-attachments/assets/606b73d7-52cb-4477-a328-89ba5b1563d1) |

### Manage and navigate through opened tabs

Comming soon...

### Running javascript

Comming soon...

## Interacting with the page elements

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

There is some abstractions that implements actions and rules for specific elements. They is listed below.

- `Element`, for any element
- [`InputElement`](#inputs), for fillable inputs (`<input .../>`)
- [`FileInputElement`](#file-inputs), for file inputs (`<input type="file" .../>`)
- [`SelectElement`](#selects), for selects (`<select .../>`)
- [`ListElement`](#lists), for ordered and unordered lists (`<ol .../>`, `<ul .../>`)
- [`ButtonElement`](#buttons-and-links), for buttons and links (`<button .../>`, `<a .../>`)
- [`FormElement`](#forms), for forms (`<form .../>`)
- [`TableElement`](#tables), for tables (`<table .../>`)
- [`MediaElement`](#medias), for any media like images and videos

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
'form form-styled'

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

### Inputs

Interactions with `input` and `textarea` tags.

```python
# Gets the right element class for the xpath
>>> my_input = web.element('//*[id="myInput"]')
>>> type(my_input)
fastrpa.core.elements.InputElement

# Try to get an InputElement and raise an ElementNotCompatible exception if the element isn't an input
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

### File inputs

Interactions with `input` with attribute `type="file"`.

```python
# Gets the right element class for the xpath
>>> my_input = web.element('//*[id="myFileInput"]')
>>> type(my_input)
fastrpa.core.elements.FileInputElement

# Try to get a FileInputElement and raise an ElementNotCompatible exception if the element isn't an file input
>>> my_input = web.file_input('//*[id="myFileInput"]')
>>> type(my_input)
fastrpa.core.elements.FileInputElement

# Attach a local file
>>> my_input.attach_file('/home/user/picture.png')

# Attach a file from the web
>>> my_input.attach_file('https://website.com/picture.png')
```

### Selects

Interactions with `select` tag.

```python
# Gets the right element class for the xpath
>>> my_select = web.element('//*[id="mySelect"]')
>>> type(my_select)
fastrpa.core.elements.SelectElement

# Try to get a SelectElement and raise an ElementNotCompatible exception if the element isn't an select input
>>> my_select = web.file_input('//*[id="mySelect"]')
>>> type(my_select)
fastrpa.core.elements.SelectElement

# Get all options from the select
>>> my_select.options
[Option(value='1', label='Option 1'),
 Option(value='2', label='Option 2')]

# Get just the options values
>>> my_select.options_values
['1', '2']

# Get just the options labels
>>> my_select.options_labels
['Option 1', 'Option 2']

# Select the option by label
>>> my_select.select('Option 1')

# Select the option by value
>>> my_select.select(value='1')

# Check if an option exists, by label and value
>>> 'Option 3' in my_select
False

# Check if an option exists, just by label
>>> my_select.has_option('Option 3')
False

# Check if an option exists, just by value
>>> my_select.has_option(value='3')
False
```

### Lists

Need to write.

### Buttons and links

Need to write.

### Forms

Need to write.

### Tables

Need to write.

### Medias

Need to write.
