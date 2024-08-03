---
description: Learn how to easily manage and navigate through tabs on the browser.
---

To manage and navigate through browse tabs, use the following methods.

## Accessing the object

```python linenums="1"
app = FastRPA()
web = app.browse('https:...')
type(web.tabs)
```

```python title="Output"
fastrpa.core.tabs.Tabs
```

## Reference

### Get opened tabs

```python linenums="1"
web.tabs.list
```

```python title="Output"
['AD9B396BF70C366D8A1FDE5450699D41', ...]
```

### Get current tab

```python linenums="1"
web.tabs.current
```

```python title="Output"
'AD9B396BF70C366D8A1FDE5450699D41'
```

### Get current tab index

```python linenums="1"
web.tabs.current_index
```

```python title="Output"
0
```

### Get the opened tabs count

```python linenums="1"
len(web.tabs)
```

```python title="Output"
5
```

### Open a new tab

This method also switch to the new tab and returns the new tab id.

```python linenums="1"
web.tabs.new()
```

```python title="Output"
'AD9B396BF70C366D8A1FDE5450699D41'
```

### Close the current tab

```python linenums="1"
web.tabs.close()
```

### Check if a tab is opened

```python linenums="1"
'AD9B396BF70C366D8A1FDE5450699D41' in web.tabs
```

```python title="Output"
True
```