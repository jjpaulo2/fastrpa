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
from fastrpa import FastRPA
from selenium.webdriver import Firefox, FirefoxOptions

options = FirefoxOptions()
options.add_argument(...)
options.add_argument(...)

webdriver = Firefox(options)
app = FastRPA(webdriver)
```

## The FastRPA instance

This is just a configuration object. You will need it just to start your web navegation.

```python
from fastrpa import FastRPA

app = FastRPA()
web = app.browse('https:...')
type(web)
<<< fastrpa.app.Web
```

## Interacting with the current page

Once you have a `Web` object, you are able to browse on the web. The `Web` class is a abstraction of main browser and user functions.

It includes, managing:

- `keyboard`, to send key pressing events on the current page
- `timer`, to wait for some events on the current page
- `cookies`, to manage cookies on the current page
- `screenshot`, to download screenshots and prints from the current page
- `tabs`, to manage and navigate through the current opened tabs
- `console`, to run javascript on the current page

You can access these abstractions by calling it from the `Web` object.

```python
web.keyboard
>>> <fastrpa.core.keyboard.Keyboard at 0x...>

web.timer
>>> <fastrpa.core.timer.Timer at 0x...>

web.cookies
>>> <fastrpa.core.cookies.Cookies at 0x...>

web.screenshot
>>> <fastrpa.core.screenshot.Screenshot at 0x...>

web.tabs
>>> <fastrpa.core.tabs.Tabs at 0x...>

web.console
>>> <fastrpa.core.console.Console at 0x...>
```

### Pressing keys

You can send simple pressing key events to the current page, by using the methods below.

- `Web.keyboard.esc()`
- `Web.keyboard.tab()`
- `Web.keyboard.enter()`

### Waiting for events

You can wait some time before or after execute some action with the automation. This method is just a simple proxy for `time.sleep`, to remove the need of more one import.

- `Web.timer.wait_seconds(seconds)`

You can also wait for element visibility. By default the timeout is 15 seconds, but you can also specify it.

```python
app = FastRPA()
web = app.browse('https:...')

# Wait a maximum of 15 seconds until a button is present
web.timer.wait_until_present('//button[@id="myBtn"]')

# Wait a maximum of custom seconds until a button is present
web.timer.wait_until_present('//button[@id="myBtn"]', 30)

# Wait a maximum of 15 seconds until a button is hide
web.timer.wait_until_hide('//button[@id="myBtn"]')

# Wait a maximum of custom seconds until a button is hide
web.timer.wait_until_hide('//button[@id="myBtn"]', 30)
```

### Managing cookies

Follow the examples below to manage cookies on the current domain.

```python
app = FastRPA()
web = app.browse('https:...')

# Get the list of cookies on the current domain
web.cookies.list
>>> [Cookie(...), Cookie(...)]

# Get the list of names from the cookies on the current domain
web.cookies.list_names
>>> ['JSESSIONID', '_ga', ...]

# Check if a cookie exists on the current domain
'my_cookie' in web.cookies
>>> True

# Check if a cookie stores some value
web.cookies.check('my_cookie', 'value')
>>> False

# Get a cookie on the current domain
web.cookies.get('my_cookie')
>>> Cookie(name='...', value='...', domain='...', path='/', secure=True, http_only=True, same_site='Strict')

# Try to get a cookie that does not exist the current domain
web.cookies.get('my_cookie')
>>> None

# Add a new cookie on the current domain
web.cookies.add('my_cookie', 'value', secure=False)
>>> Cookie(name='my_cookie', value='value', domain='...', path='/', secure=False, http_only=True, same_site='Strict')
```

### Take screenshots and prints

By default, all screenshot methods save the files in the current active directory.

```python
app = FastRPA()
web = app.browse('https:...')

# Take a screenshot just containing the current viewport size
web.screenshot.viewport()

# Take a screenshot just containing the current viewport size, and save the file in the specified path
web.screenshot.viewport('/my/screenshot/path.png')

# Take a screenshot containing the complete page
web.screenshot.full_page()

# Take a screenshot containing the complete page, and save the file in the specified path
web.screenshot.full_page('/my/screenshot/path.png')
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

Need to write.

### Inputs

Need to write.

### File inputs

Need to write.

### Selects

Need to write.

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
