---
description: Interações com tags `ol` e `ul`.
---

Interações com tags `ol` e `ul`.

## Lendo o elemento

### Obtendo a classe correta do elemento para o xpath

```python linenums="1"
my_list = web.element('//*[id="myList"]')
type(my_select)
```

```python title="Saída"
fastrpa.core.elements.ListElement
```

### Tentando obter um `ListElement`

```python linenums="1"
my_list = web.list('//*[id="myList"]')
type(my_select)
```

```python title="Saída"
fastrpa.core.elements.ListElement
```

## Referência

### Verificar se a lista é ordenada

```python linenums="1"
my_list.is_ordered
```

```python title="Saída"
True
```

### Obter todos os itens da lista

```python linenums="1"
my_list.items
```

```python title="Saída"
{'1': 'Item 1',
 '2': 'Item 2'}
```

### Obter apenas os ids dos itens

```python linenums="1"
my_list.items_ids
```

```python title="Saída"
['1', '2']
```

### Obter apenas os rótulos dos itens

```python linenums="1"
my_list.items_labels
```

```python title="Saída"
['Item 1', 'Item 2']
```

### Clicar no item pelo rótulo

```python linenums="1"
my_list.click_in_item('Item 1')
```

### Clicar no item pelo id

```python linenums="1"
my_list.click_in_item(id='1')
```

### Verificar se um item existe, pelo rótulo e valor

```python linenums="1"
'Item 3' in my_list
```

```python title="Saída"
False
```

### Verificar se um item existe, apenas pelo rótulo

```python linenums="1"
my_list.has_item('Option 3')
```

```python title="Saída"
False
```

### Verificar se um item existe, apenas pelo id

```python linenums="1"
my_list.has_item(id='3')
```

```python title="Saída"
False
```

### Imprimir os itens da lista

!!! warning "Extra necessário!"
    Para usar este método, você precisa instalar os extras **debug**, como [mostrado aqui](../index.md#installation), com o comando `pip install "fastrpa[debug]"`.

```python linenums="1"
my_list.print()
```

```python title="Saída"
[@id="myList"]
├── [1] Item 1
├── [2] Item 2
├── [3] Item 3
└── [4] Item 4
```
