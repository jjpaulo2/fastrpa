You can wait some time before or after execute some action with the automation.

## Accessing the object

```python linenums="1"
app = FastRPA(timeout=60)
web = app.browse('https:...')
type(web.wait)
```

```python title="Output"
fastrpa.core.wait.Wait
```

## Shortcuts

### Wait some seconds

The method is just a simple proxy for `time.sleep`, to remove the need of one more import.

```python linenums="1"
web.wait.seconds(10)
```

## Reference

!!!info
    By default, all methods get the default **timeout** from **FastRPA** instance. Every methods listed below, accepts an last parameter called **timeout** to specify a custom value.

### Wait until element is present

```python linenums="1"
web.wait.is_present('//button[@id="myBtn"]')
```

To specify a custom `timeout`, you can do this in every method below.

```python linenums="1"
web.wait.is_present('//button[@id="myBtn"]', 60)
web.wait.is_present('//button[@id="myBtn"]', timeout=60)
```

### Wait until element **not** is present

```python linenums="1"
web.wait.not_is_present('//button[@id="myBtn"]')
```

### Wait until element is clickable

```python linenums="1"
web.wait.is_clickable('//button[@id="myBtn"]')
```

### Wait until element **not** is clickable

```python linenums="1"
web.wait.not_is_clickable('//button[@id="myBtn"]')
```

### Wait until element is hidden

```python linenums="1"
web.wait.is_hidden('//button[@id="myBtn"]')
```

### Wait until element **not** is hidden

```python linenums="1"
web.wait.not_is_hidden('//button[@id="myBtn"]')
```

### Wait until element contains text

```python linenums="1"
web.wait.contains_text('//button[@id="myBtn"]', 'any text')
```

### Wait until element **not** contains text

```python linenums="1"
web.wait.not_contains_text('//button[@id="myBtn"]', 'any text')
```

### Wait until URL contains some text

```python linenums="1"
web.wait.url_contains('mysite.com/mypath')
```

### Wait until URL **not** contains some text

```python linenums="1"
web.wait.not_url_contains('mysite.com/mypath')
```

### Wait until title contains some text

```python linenums="1"
web.wait.title_contains('my page')
```

### Wait until title **not** contains some text

```python linenums="1"
web.wait.not_title_contains('my page')
```