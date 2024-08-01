Interactions with `table` tag.

## Reading the element

### Getting the right element class for the xpath

```python
>>> my_table = web.element('//*[id="myTable"]')
>>> type(my_select)
fastrpa.core.elements.TableElement
```

### Try to get a `TableElement`

```python
>>> my_table = web.button('//*[id="myTable"]')
>>> type(my_select)
fastrpa.core.elements.TableElement
```

## Reference

### Get the headers values

```python
>>> my_table.headers
['Company', 'Contact', 'Country']
```

### Get the rows values

```python
>>> my_table.rows
[['Alfreds Futterkiste', 'Maria Anders', 'Germany'],
 ['Centro comercial Moctezuma', 'Francisco Chang', 'Mexico'],
 ...]
```

### Get all values from one column, by column name

```python
>>> my_table.column_values('Company')
['Alfreds Futterkiste',
 'Centro comercial Moctezuma',
 ...]
```

### Get all values from one column, by column index

```python
>>> my_table.column_values(index=0)
['Alfreds Futterkiste',
 'Centro comercial Moctezuma',
 ...]
```

### Check if a value exists in one of the table cells

```python
>>> 'Cell content' in my_table
False
```

### Print the table in console

> To use this method, you need to install the **\[debug\]** extras, as [shown here](../index.md#installation).

```python
>>> my_table.print()
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