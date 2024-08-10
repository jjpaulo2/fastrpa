---
description: Interações com a tag `table`.
---

Interações com a tag `table`.

## Lendo o elemento

### Obtendo a classe correta do elemento para o xpath

```python linenums="1"
my_table = web.element('//*[id="myTable"]')
type(my_table)
```

```python title="Saída"
fastrpa.core.elements.TableElement
```

### Tentando obter um `TableElement`

```python linenums="1"
my_table = web.button('//*[id="myTable"]')
type(my_table)
```

```python title="Saída"
fastrpa.core.elements.TableElement
```

## Referência

### Obter os valores dos cabeçalhos

```python linenums="1"
my_table.headers
```

```python title="Saída"
['Company', 'Contact', 'Country']
```

### Obter os valores das linhas

```python linenums="1"
my_table.rows
```

```python title="Saída"
[['Alfreds Futterkiste', 'Maria Anders', 'Germany'],
 ['Centro comercial Moctezuma', 'Francisco Chang', 'Mexico'],
 ...]
```

### Obter todos os valores de uma coluna, pelo nome da coluna

```python linenums="1"
my_table.column_values('Company')
```

```python title="Saída"
['Alfreds Futterkiste',
 'Centro comercial Moctezuma',
 ...]
```

### Obter todos os valores de uma coluna, pelo índice da coluna

```python linenums="1"
my_table.column_values(index=0)
```

```python title="Saída"
['Alfreds Futterkiste',
 'Centro comercial Moctezuma',
 ...]
```

### Verificar se um valor existe em uma das células da tabela

```python linenums="1"
'Cell content' in my_table
```

```python title="Saída"
False
```

### Imprimir a tabela no console

!!! warning "Extra necessário!"
    Para usar este método, você precisa instalar os extras **debug**, como [mostrado aqui](../index.md#installation), com o comando `pip install "fastrpa[debug]"`.

```python linenums="1"
my_table.print()
```

```python title="Saída"
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
