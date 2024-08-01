Interactions with `ol` and `ul` tags.

## Reading the element

### Getting the right element class for the xpath

```python linenums="1"
my_list = web.element('//*[id="myList"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.ListElement
```

### Try to get a `ListElement`

```python linenums="1"
my_list = web.list('//*[id="myList"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.ListElement
```

## Reference

### Check if the list is ordered

```python linenums="1"
my_list.is_ordered
```

```python title="Output"
True
```

### Get all items from the list

```python linenums="1"
my_list.items
```

```python title="Output"
{'1': 'Item 1',
 '2': 'Item 2'}
```

### Get just the items ids

```python linenums="1"
my_list.items_ids
```

```python title="Output"
['1', '2']
```

### Get just the items labels

```python linenums="1"
my_list.items_labels
```

```python title="Output"
['Item 1', 'Item 2']
```

### Click in the item by label

```python linenums="1"
my_list.click_in_item('Item 1')
```

### Click in the item by id

```python linenums="1"
my_list.click_in_item(id='1')
```

### Check if an item exists, by label and value

```python linenums="1"
'Item 3' in my_list
```

```python title="Output"
False
```

### Check if an item exists, just by label

```python linenums="1"
my_list.has_item('Option 3')
```

```python title="Output"
False
```

### Check if an item exists, just by id

```python linenums="1"
my_list.has_item(id='3')
```

```python title="Output"
False
```
### Print the items of the list

!!! warning "Extra needed!"
    To use this method, you need to install the **debug** extras, as [shown here](../index.md#installation), with the command `pip install fastrpa[debug]`.

```python linenums="1"
my_list.print()
```

```python title="Output"
[@id="myList"]
├── [1] Item 1
├── [2] Item 2
├── [3] Item 3
└── [4] Item 4
```