Interactions with `select` tag.

## Reading the element

### Getting the right element class for the xpath

```python
>>> my_select = web.element('//*[id="mySelect"]')
>>> type(my_select)
fastrpa.core.elements.SelectElement
```

### Try to get a `SelectElement`

```python
>>> my_select = web.select('//*[id="mySelect"]')
>>> type(my_select)
fastrpa.core.elements.SelectElement
```

## Reference

### Get all options from the select

```python
>>> my_select.options
{'1': 'Option 1',
 '2': 'Option 2'}
```

### Get just the options values

```python
>>> my_select.options_values
['1', '2']
```

### Get just the options labels

```python
>>> my_select.options_labels
['Option 1', 'Option 2']
```

### Select the option by label

```python
>>> my_select.select('Option 1')
```

### Select the option by value

```python
>>> my_select.select(value='1')
```

### Get the current value from the select

```python
>>> my_select.current
('1', 'Option 1')
```

### Check if an option exists, by label and value

```python
>>> 'Option 3' in my_select
False
```

### Check if an option exists, just by label

```python
>>> my_select.has_option('Option 3')
False
```

### Check if an option exists, just by value

```python
>>> my_select.has_option(value='3')
False
```

### Print the options of the select

> To use this method, you need to install the **\[debug\]** extras, as [shown here](../index.md#installation).

```python
>>> my_select.print()
[@id="mySelect"]
├── [1] Option 1
├── [2] Option 2
├── [3] Option 3
└── [4] Option 4
```