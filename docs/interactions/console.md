To run javascript on the current page, you can use the following methods.

## Accessing the object

```python linenums="1"
app = FastRPA()
web = app.browse('https:...')
type(web.console)
```

```python title="Output"
fastrpa.core.console.Console
```

## Reference

### Evaluate a simple expression

```python linenums="1"
web.console.evaluate('2 + 2')
```

```python title="Output"
4
```

### Run multi line scripts

```python linenums="1"
web.console.run([
    'button = document.getElementById("myButton")',
    'button.click()'
])
```

### Run a javascript file

```python linenums="1"
web.console.run_script('/path/to/script.js')
```
