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
    - [Images](#images)


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

```python
# The current URL from the browser
>>> web.url
'https://www.site.com/mypage'

# The domain from the current URL
>>> web.domain
'www.site.com'

# The title from the current page
>>> web.title
'My website'

# Navigate to an URL
>>> web.browse('https://www.site.com/another_page')

# Refresh the current page
>>> web.refresh()

# Check if an element is interactive on the screen
>>> web.is_interactive('//*[@id="myElement"]')
False

# Get the from text content from an element
>>> web.read('//*[@id="myElement"]')
'Any text'

```

You can also, manage the following items:

- [`keyboard`](#pressing-keys), to send key pressing events on the current page
- [`wait`](#waiting-for-events), to wait for some events on the current page
- [`cookies`](#managing-cookies), to manage cookies on the current page
- [`screenshot`](#take-screenshots-and-prints), to download screenshots and prints from the current page
- [`tabs`](#manage-and-navigate-through-opened-tabs), to manage and navigate through the current opened tabs
- [`console`](#running-javascript), to run javascript on the current page

You can access these abstractions by calling it from the `Web` object.

```python
>>> web.keyboard
<fastrpa.core.keyboard.Keyboard at 0x...>

>>> web.wait
<fastrpa.core.wait.Wait at 0x...>

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

You can send keyboard events to the current page, by using the methods below.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# To send a simple key press event
>>> web.keyboad.press('control')
>>> web.keyboad.press('escape')
>>> web.keyboad.press('enter')

# To send a keyboard shortcut event
>>> web.keyboad.shortcut('control', 'a')
>>> web.keyboad.shortcut('control', 'shift', 'c')

# To see the available command keyboard keys
>>> web.keyboad.keys
['ADD',
 'ALT',
 'ARROW_DOWN',
 'ARROW_LEFT',
 'ARROW_RIGHT',
 'ARROW_UP',
 'BACKSPACE',
 'BACK_SPACE',
 ...
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

# Delete a cookie on the current domain
>>> web.cookies.delete('my_cookie')
```

### Take screenshots and prints

By default, all screenshot methods save the files in the current active directory.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# Get a PNG bytes content from the current viewport size
>>> web.screenshot.image
b'\x89PNG\r\n\x1a\n\x00\x00...'

# Save a PNG file from the current viewport size
>>> web.screenshot.save_image()
>>> web.screenshot.save_image('/my/screenshot/path.png')

# Get a PNG bytes content from the complete page
>>> web.screenshot.full_page_image
b'\x89PNG\r\n\x1a\n\x00\x00...'

# Save a PNG file from the complete page
>>> web.screenshot.save_full_page()
>>> web.screenshot.save_full_page('/my/screenshot/path.png')
```

You can see examples of both screenshot methods below.

| `web.screenshot.image` | `web.screenshot.full_page_image` |
|-|-|
| ![image](https://github.com/user-attachments/assets/ec5abfe0-5858-450a-a938-9fff58f89b86) | ![image](https://github.com/user-attachments/assets/606b73d7-52cb-4477-a328-89ba5b1563d1) |

### Manage and navigate through opened tabs

To manage and navigate through browse tabs, use the following methods.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# Get opened tabs ids
>>> web.tabs.list
['AD9B396BF70C366D8A1FDE5450699D41', ...]

# Get current tab id
>>> web.tabs.current
'AD9B396BF70C366D8A1FDE5450699D41'

# Get current tab index
>>> web.tabs.current_index
0

# Get the opened tabs count
>>> web.tabs.count
5

# Get the opened tabs count
>>> len(web.tabs)
5

# Open a new tab, switch to it and return the new tab id
>>> web.tabs.new()
'AD9B396BF70C366D8A1FDE5450699D41'

# Close the current tab
>>> web.tabs.close()

# Check if a tab is opened
>>> 'AD9B396BF70C366D8A1FDE5450699D41' in web.tabs
True
```

### Running javascript

To run javascript on the current page, you can use the following methods.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# To just evaluate a simple expression
>>> web.console.evaluate('2 + 2')
4

# To run complex and multi line scripts, use this
>>> web.console.run(['button = document.getElementById("myButton")', 'button.click()'])

# To run a script file, use this
>>> web.console.run_script('/path/to/script.js')
```

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

### Inputs

Interactions with `input` and `textarea` tags.

```python
# Gets the right element class for the xpath
>>> my_input = web.element('//*[id="myInput"]')
>>> type(my_input)
fastrpa.core.elements.InputElement

# Try to get an InputElement
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

# Try to get a FileInputElement
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

# Try to get a SelectElement
>>> my_select = web.select('//*[id="mySelect"]')
>>> type(my_select)
fastrpa.core.elements.SelectElement

# Get all options from the select
>>> my_select.options
{'1': 'Option 1',
 '2': 'Option 2'}

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

# Get the current value from the select
>>> my_select.current
('1', 'Option 1')

# Check if an option exists, by label and value
>>> 'Option 3' in my_select
False

# Check if an option exists, just by label
>>> my_select.has_option('Option 3')
False

# Check if an option exists, just by value
>>> my_select.has_option(value='3')
False

# Print the options of the select
>>> my_select.print()
[@id="mySelect"]
├── [1] Option 1
├── [2] Option 2
├── [3] Option 3
└── [4] Option 4
```

### Lists

Interactions with `ol` and `ul` tags.

```python
# Gets the right element class for the xpath
>>> my_list = web.element('//*[id="myList"]')
>>> type(my_select)
fastrpa.core.elements.ListElement

# Try to get a ListElement
>>> my_list = web.list('//*[id="myList"]')
>>> type(my_select)
fastrpa.core.elements.ListElement

# Check if the list is ordered
>>> my_list.is_ordered
True

# Get all items from the list
>>> my_list.items
{'1': 'Item 1',
 '2': 'Item 2'}

# Get just the items ids
>>> my_list.items_ids
['1', '2']

# Get just the items labels
>>> my_list.items_labels
['Item 1', 'Item 2']

# Click in the item by label
>>> my_list.click_in_item('Item 1')

# Click in the item by id
>>> my_list.click_in_item(id='1')

# Check if an item exists, by label and value
>>> 'Item 3' in my_list
False

# Check if an item exists, just by label
>>> my_list.has_item('Option 3')
False

# Check if an item exists, just by id
>>> my_list.has_item(id='3')
False

# Print the items of the list
>>> my_list.print()
[@id="myList"]
├── [1] Item 1
├── [2] Item 2
├── [3] Item 3
└── [4] Item 4
```

### Buttons and links

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

### Forms

Interactions with `form` tag.

```python
# Gets the right element class for the xpath
>>> my_form = web.element('//*[id="myForm"]')
>>> type(my_select)
fastrpa.core.elements.FormElement

# Try to get a FormElement
>>> my_form = web.button('//*[id="myForm"]')
>>> type(my_select)
fastrpa.core.elements.FormElement

# Get form method
>>> my_form.method
'POST'

# Get form action
>>> my_form.action
'https://www.mysite.com/form'

# Get form type
>>> my_form.type
'application/x-www-form-urlencoded'

# Submit the form
>>> my_form.submit()

# Submit the form by clicking in a button
>>> my_form_button = web.button('//*[id="formSubmit"]')
>>> my_form.submit(my_form_button)
```

Forms also accept success conditions to ensure your form was properly filled. If any condition fail, the form raises a `FormException`.

```python
# Set success by redireto to any url
>>> my_form.set_success_condition(redirect_url='https:://.../success_page.html')

# Set success by any element on the page
>>> my_form.set_success_condition(elements_to_find=['//div[@id="success_message"]'])

# Set success by any text on the page
>>> my_form.set_success_condition(text_to_find=['Success!'])

# Set success by all available conditions
>>> my_form.set_success_condition(redirect_url='https:://.../success_page.html', elements_to_find=['//div[@id="success_message"]'], text_to_find=['Success!'])

# Submit a form successfully
>>> my_form.submit()

# Fails a form submission
>>> my_form.submit()
Traceback (most recent call last):
    ...
FormException: The form submission got an error!
Condition [redirect_url, https://...] not satisfied!
```

### Tables

Interactions with `table` tag.

```python
# Gets the right element class for the xpath
>>> my_table = web.element('//*[id="myTable"]')
>>> type(my_select)
fastrpa.core.elements.TableElement

# Try to get a TableElement
>>> my_table = web.button('//*[id="myTable"]')
>>> type(my_select)
fastrpa.core.elements.TableElement

# Get the headers values
>>> my_table.headers
['Company', 'Contact', 'Country']

# Get the rows values
>>> my_table.rows
[['Alfreds Futterkiste', 'Maria Anders', 'Germany'],
 ['Centro comercial Moctezuma', 'Francisco Chang', 'Mexico'],
 ...]

# Get all values from one column, by column name
>>> my_table.column_values('Company')
['Alfreds Futterkiste',
 'Centro comercial Moctezuma',
 ...]

# Get all values from one column, by column index
>>> my_table.column_values(index=0)
['Alfreds Futterkiste',
 'Centro comercial Moctezuma',
 ...]

# Check if a value exists in one of the table cells
>>> 'Cell content' in my_table
False

# Print the table in console
>>> my_table.print()
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Company                      ┃ Contact          ┃ Country ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ Alfreds Futterkiste          │ Maria Anders     │ Germany │
│ Centro comercial Moctezuma   │ Francisco Chang  │ Mexico  │
│ Ernst Handel                 │ Roland Mendel    │ Austria │
│ Island Trading               │ Helen Bennett    │ UK      │
│ Laughing Bacchus Winecellars │ Yoshi Tannamuri  │ Canada  │
│ Magazzini Alimentari Riuniti │ Giovanni Rovelli │ Italy   │
└──────────────────────────────┴──────────────────┴─────────┘
```

### Images

Interactions with `img` tag.

```python
# Gets the right element class for the xpath
>>> my_image = web.element('//*[id="myImage"]')
>>> type(my_select)
fastrpa.core.elements.TableElement

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