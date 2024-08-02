---
description: Interactions with <table> tag.
---

Interactions with `table` tag.

## Reading the element

### Getting the right element class for the xpath

```python linenums="1"
my_table = web.element('//*[id="myTable"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.TableElement
```

### Try to get a `TableElement`

```python linenums="1"
my_table = web.button('//*[id="myTable"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.TableElement
```

## Reference

### Get the headers values

```python linenums="1"
my_table.headers
```

```python title="Output"
['Company', 'Contact', 'Country']
```

### Get the rows values

```python linenums="1"
my_table.rows
```

```python title="Output"
[['Alfreds Futterkiste', 'Maria Anders', 'Germany'],
 ['Centro comercial Moctezuma', 'Francisco Chang', 'Mexico'],
 ...]
```

### Get all values from one column, by column name

```python linenums="1"
my_table.column_values('Company')
```

```python title="Output"
['Alfreds Futterkiste',
 'Centro comercial Moctezuma',
 ...]
```

### Get all values from one column, by column index

```python linenums="1"
my_table.column_values(index=0)
```

```python title="Output"
['Alfreds Futterkiste',
 'Centro comercial Moctezuma',
 ...]
```

### Check if a value exists in one of the table cells

```python linenums="1"
'Cell content' in my_table
```

```python title="Output"
False
```

### Print the table in console

!!! warning "Extra needed!"
    To use this method, you need to install the **debug** extras, as [shown here](../index.md#installation), with the command `pip install fastrpa[debug]`.

```python linenums="1"
my_table.print()
```

```python title="Output"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Company                      ┃ Contact          ┃ Country ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ Alfreds Futterkiste          │ Maria Anders     │ Germany │
│ Centro comercial Moctezuma   │ Francisco Chang  │ Mexico  │
│ Ernst Handel                 │ Roland Mendel    │ Austria │
│ Island Trading               │ Helen Bennett    │ UK      │
│ Laughing Bacchus Winecellars │ Yoshi Tannamuri  │ Canada  │
│ Magazzini Alimentari Riuniti │ Giovanni Rovelli │ Italy   │
└──────────────────────────────┴──────────────────┴─────────┘
```