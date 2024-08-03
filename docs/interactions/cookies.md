---
description: Learn how to easily manage cookies on the current domain.
---

An abstraction to manage cookies on the current domain.

## Accessing the object

```python linenums="1"
app = FastRPA()
web = app.browse('https:...')
type(web.cookies)
```

```python title="Output"
fastrpa.core.cookies.Cookies
```

## Reference

### Get the list of cookies on the current domain

```python linenums="1"
web.cookies.list
```

```python title="Output"
[Cookie(...), Cookie(...)]
```

### Get the list of names from the cookies on the current domain

```python linenums="1"
web.cookies.list_names
```

```python title="Output"
['JSESSIONID', '_ga', ...]
```

### Check if a cookie exists on the current domain

```python linenums="1"
'my_cookie' in web.cookies
```

```python title="Output"
True
```

### Check if a cookie stores some value

```python linenums="1"
web.cookies.check('my_cookie', 'value')
```

```python title="Output"
False
```

### Get a cookie on the current domain

```python linenums="1"
web.cookies.get('my_cookie')
```

```python title="Output"
Cookie(name='...', value='...', domain='...', path='/', secure=True, http_only=True, same_site='Strict')
```

### Get a cookie that does not exist the current domain

```python linenums="1"
web.cookies.get('my_cookie')
```

```python title="Output"
None
```

### Add a new cookie on the current domain

```python linenums="1"
web.cookies.add('my_cookie', 'value')
```

```python title="Output"
Cookie(name='my_cookie', value='value', domain='...', path='/', secure=False, http_only=True, same_site='Strict')
```

### Delete a cookie on the current domain

```python linenums="1"
web.cookies.delete('my_cookie')
```
