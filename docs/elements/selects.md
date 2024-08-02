---
description: Interactions with <select> tag.
---

Interactions with `select` tag.

## Reading the element

### Getting the right element class for the xpath

```python linenums="1"
my_select = web.element('//*[id="mySelect"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.SelectElement
```

### Try to get a `SelectElement`

```python linenums="1"
my_select = web.select('//*[id="mySelect"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.SelectElement
```

## Reference

### Get all options from the select

```python linenums="1"
my_select.options
```

```python title="Output"
{'1': 'Option 1',
 '2': 'Option 2'}
```

### Get just the options values

```python linenums="1"
my_select.options_values
```

```python title="Output"
['1', '2']
```

### Get just the options labels

```python linenums="1"
my_select.options_labels
```

```python title="Output"
['Option 1', 'Option 2']
```

### Select the option by label

```python linenums="1"
my_select.select('Option 1')
```

### Select the option by value

```python linenums="1"
my_select.select(value='1')
```

### Get the current value from the select

```python linenums="1"
my_select.current
```

```python title="Output"
('1', 'Option 1')
```

### Check if an option exists, by label and value

```python linenums="1"
'Option 3' in my_select
```

```python title="Output"
False
```

### Check if an option exists, just by label

```python linenums="1"
my_select.has_option('Option 3')
```

```python title="Output"
False
```

### Check if an option exists, just by value

```python linenums="1"
my_select.has_option(value='3')
```

```python title="Output"
False
```

### Print the options of the select

!!! warning "Extra needed!"
    To use this method, you need to install the **debug** extras, as [shown here](../index.md#installation), with the command `pip install fastrpa[debug]`.

```python linenums="1"
my_select.print()
```

```python title="Output"
[@id="mySelect"]
├── [1] Option 1
├── [2] Option 2
├── [3] Option 3
└── [4] Option 4
```