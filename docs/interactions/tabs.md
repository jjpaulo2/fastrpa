To manage and navigate through browse tabs, use the following methods.

```python
>>> app = FastRPA()
>>> web = app.browse('https:...')

# Get opened tabs ids
>>> web.tabs.list
['AD9B396BF70C366D8A1FDE5450699D41', ...]

# Get current tab id
>>> web.tabs.current
'AD9B396BF70C366D8A1FDE5450699D41'

# Get current tab index
>>> web.tabs.current_index
0

# Get the opened tabs count
>>> web.tabs.count
5

# Get the opened tabs count
>>> len(web.tabs)
5

# Open a new tab, switch to it and return the new tab id
>>> web.tabs.new()
'AD9B396BF70C366D8A1FDE5450699D41'

# Close the current tab
>>> web.tabs.close()

# Check if a tab is opened
>>> 'AD9B396BF70C366D8A1FDE5450699D41' in web.tabs
True
```