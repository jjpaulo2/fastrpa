Interactions with `ol` and `ul` tags.

```python
# Gets the right element class for the xpath
>>> my_list = web.element('//*[id="myList"]')
>>> type(my_select)
fastrpa.core.elements.ListElement

# Try to get a ListElement
>>> my_list = web.list('//*[id="myList"]')
>>> type(my_select)
fastrpa.core.elements.ListElement

# Check if the list is ordered
>>> my_list.is_ordered
True

# Get all items from the list
>>> my_list.items
{'1': 'Item 1',
 '2': 'Item 2'}

# Get just the items ids
>>> my_list.items_ids
['1', '2']

# Get just the items labels
>>> my_list.items_labels
['Item 1', 'Item 2']

# Click in the item by label
>>> my_list.click_in_item('Item 1')

# Click in the item by id
>>> my_list.click_in_item(id='1')

# Check if an item exists, by label and value
>>> 'Item 3' in my_list
False

# Check if an item exists, just by label
>>> my_list.has_item('Option 3')
False

# Check if an item exists, just by id
>>> my_list.has_item(id='3')
False

# Print the items of the list
>>> my_list.print()
[@id="myList"]
├── [1] Item 1
├── [2] Item 2
├── [3] Item 3
└── [4] Item 4
```