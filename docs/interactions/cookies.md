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