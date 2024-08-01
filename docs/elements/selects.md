Interactions with `select` tag.

```python
# Gets the right element class for the xpath
>>> my_select = web.element('//*[id="mySelect"]')
>>> type(my_select)
fastrpa.core.elements.SelectElement

# Try to get a SelectElement
>>> my_select = web.select('//*[id="mySelect"]')
>>> type(my_select)
fastrpa.core.elements.SelectElement

# Get all options from the select
>>> my_select.options
{'1': 'Option 1',
 '2': 'Option 2'}

# Get just the options values
>>> my_select.options_values
['1', '2']

# Get just the options labels
>>> my_select.options_labels
['Option 1', 'Option 2']

# Select the option by label
>>> my_select.select('Option 1')

# Select the option by value
>>> my_select.select(value='1')

# Get the current value from the select
>>> my_select.current
('1', 'Option 1')

# Check if an option exists, by label and value
>>> 'Option 3' in my_select
False

# Check if an option exists, just by label
>>> my_select.has_option('Option 3')
False

# Check if an option exists, just by value
>>> my_select.has_option(value='3')
False

# Print the options of the select
>>> my_select.print()
[@id="mySelect"]
├── [1] Option 1
├── [2] Option 2
├── [3] Option 3
└── [4] Option 4
```