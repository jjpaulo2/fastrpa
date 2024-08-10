---
description: Learn how to easily access the Selenium and requests native objects.
---

In this page, you will learn to access selenium and requests objects directly, to implement your own abstractions, if FastRPA does not deliver some feature to you.

## Get `WebDriver` instances

Both `FastRPA` and `Web` have a `webdriver` property that always return a `WebDriver` instance. An example below shows an access to the object from the `FastRPA` instance.

```python linenums="1"
app = FastRPA()
app.webdriver
```

```python title="Output"
<selenium.webdriver.remote.webdriver.WebDriver (session="...")>
```

Now, to access the object from the `Web` instance.

```python linenums="1"
web = app.web()
web.webdriver
```

```python title="Output"
<selenium.webdriver.remote.webdriver.WebDriver (session="...")>
```

## Get `WebElement` instances

Every `Element` instances have an `source` property that always must return a `WebElement` instance.

```python linenums="1"
element = web.element('//*[@id="myElement"]')
element.source
```

```python title="Output"
<selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>
```

## Get `Session` instances

The `Web` object has a session property, that always return a request's `Session` object. The session comes with all cookies from the webdriver instance.

```python linenums="1"
web = app.web()
web.session
```

```python title="Output"
<requests.sessions.Session at 0x1099352d0>
```
