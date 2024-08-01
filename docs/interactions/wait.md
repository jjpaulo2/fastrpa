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