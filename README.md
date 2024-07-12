# FastRPA

A simple to use abstraction over Selenium.

> [!WARNING]  
> This is a beta project, and is still in development. Don't use it in production, because it can raise unknown errors.

## Core concepts

- Based on Selenium
- XPath-oriented
- Easy to use

## Next steps

- [x] Forms abstraction
- [ ] Tables abstraction
- [ ] Unit tests
- [ ] Documentation 

## Before use it

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

## Examples of use

### Fill and submit a simple text form

```python
from fastrpa import FastRPA

app = FastRPA()

form_page = app.browse('http://...')

my_form = form_page.form('//form[@id="login"]')
my_form.fill('//input[@id="username"]', 'user')
my_form.fill('//input[@id="password"]', 'pass')

# To just submit the form
my_form.submit()

# To submit by clicking in a button
my_form.submit('//button[@id="submit"]')

```

### Attach a file in a form

```python
# You can easily attach files from the web
my_form.attach_file('//input[@id="photo"]', 'https://website.com/mypic.png')

# Or just local files, if you prefer
my_form.attach_file('//input[@id="photo"]', '/home/user/mypic.png')
```

### Read the available options in a select

```python
my_form.get_select_options('//select[@id="occupation"]')

[
    Option(value='1', label='Actor'),
    Option(value='2', label='Developer'),
    Option(value='3', label='Doctor'),
    Option(value='4', label='Professor'),
    ...
```

### Select an option in a select

```python
# You can just select by the text label
my_form.select_option('//select[@id="occupation"]', 'Developer')

# Or just by the value, if you prefer
my_form.select_option('//select[@id="occupation"]', value='2')

```
