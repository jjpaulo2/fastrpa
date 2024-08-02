---
title: Documentation
description: Official documentation from FastRPA. A simple to use abstraction over Selenium.
---

# FastRPA

![Python](https://img.shields.io/badge/Python-3.10_%7C_3.11_%7C_3.12-green)
[![Tests](https://github.com/jjpaulo2/fastrpa/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/jjpaulo2/fastrpa/actions/workflows/tests.yaml)
[![Documentation](https://github.com/jjpaulo2/fastrpa/actions/workflows/docs.yaml/badge.svg?branch=main)](https://github.com/jjpaulo2/fastrpa/actions/workflows/docs.yaml)
[![Publish](https://github.com/jjpaulo2/fastrpa/actions/workflows/publish.yaml/badge.svg?branch=main)](https://github.com/jjpaulo2/fastrpa/actions/workflows/publish.yaml)
[![PyPI - Version](https://img.shields.io/pypi/v/fastrpa)](https://pypi.org/project/fastrpa/)
[![Sponsor](https://img.shields.io/badge/Sponsor-FastRPA-deeppink)](https://github.com/sponsors/jjpaulo2)

A simple to use abstraction over Selenium.

- [x] **Easy to use**: complex interactions are abstracted to intuitive methods.
- [x] **Clean imports**: remove the necessity of import many packages and objects. Every automation features are accessible by methods of one main object.
- [x] **Typed**: type hints grant the code readability, and turn possible to navigate through the methods with any Intellisense tool.
- [x] **Selenium safe**: the core was developed following the Selenium best-practices. You can focus on business rules.

## Installation

To perform a basic installation, just run:

```
pip install fastrpa
```

To install also, packages to help you to debug your application, install with **debug** extras:

```
pip install "fastrpa[debug]"
```

## Your first instance

The FastRPA object, will prepare everything you need to start browse on the web. You can pass Selenium configurations to it. See [here](./selenium.md) how to do it.

```python linenums="1"
from fastrpa import FastRPA
app = FastRPA()
web = app.web()
type(web)
```

```python title="Output"
fastrpa.app.Web
```

You can also instanciate a Web object and browse to an starter URL.

```python linenums="1"
web = app.web('https://...')
```

## The Web objects

Once you have a `Web` object, you are able to browse on the web. The `Web` class is a abstraction of main browser and user functions.

### Get the current URL from the browser

```python linenums="1"
web.url
```

```python title="Output"
'https://www.site.com/mypage'
```

### Get the domain from the current URL

```python linenums="1"
web.domain
```

```python title="Output"
'www.site.com'
```

### Get the title from the current page

```python linenums="1"
web.title
```

```python title="Output"
'My website'
```

### Navigate to an URL

```python linenums="1"
web.browse('https://www.site.com/another_page')
```

### Refresh the current page

```python linenums="1"
web.refresh()
```

### Check if an element is interactive on the screen

```python linenums="1"
web.is_interactive('//*[@id="myElement"]')
```

```python title="Output"
False
```

### Get the text content from an element

```python linenums="1"
web.read('//*[@id="myElement"]')
```

```python title="Output"
'Any text'

```

## Next steps

- [Configure the selenium integration](./selenium.md)
- [Running interactions with the current page](./interactions/index.md)
- [Manipulating elements](./elements/index.md)
- [Get xpaths in a easier way](./xpath-tools.md)
- [Use the selenium/requests API directly](./low-level.md)
