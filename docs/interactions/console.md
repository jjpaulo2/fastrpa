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