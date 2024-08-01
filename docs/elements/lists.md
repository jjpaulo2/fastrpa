Interactions with `ol` and `ul` tags.

## Reading the element

### Getting the right element class for the xpath

```python
>>> my_list = web.element('//*[id="myList"]')
>>> type(my_select)
fastrpa.core.elements.ListElement
```

### Try to get a `ListElement`

```python
>>> my_list = web.list('//*[id="myList"]')
>>> type(my_select)
fastrpa.core.elements.ListElement
```

## Reference

### Check if the list is ordered

```python
>>> my_list.is_ordered
True
```

### Get all items from the list

```python
>>> my_list.items
{'1': 'Item 1',
 '2': 'Item 2'}
```

### Get just the items ids

```python
>>> my_list.items_ids
['1', '2']
```

### Get just the items labels

```python
>>> my_list.items_labels
['Item 1', 'Item 2']
```

### Click in the item by label

```python
>>> my_list.click_in_item('Item 1')
```

### Click in the item by id

```python
>>> my_list.click_in_item(id='1')
```

### Check if an item exists, by label and value

```python
>>> 'Item 3' in my_list
False
```

### Check if an item exists, just by label

```python
>>> my_list.has_item('Option 3')
False
```

### Check if an item exists, just by id

```python
>>> my_list.has_item(id='3')
False
```
### Print the items of the list

> To use this method, you need to install the **\[debug\]** extras, as [shown here](../index.md#installation).

```python
>>> my_list.print()
[@id="myList"]
├── [1] Item 1
├── [2] Item 2
├── [3] Item 3
└── [4] Item 4
```