---
description: Interações com a tag `select`.
---

Interações com a tag `select`.

## Lendo o elemento

### Obtendo a classe correta do elemento para o xpath

```python linenums="1"
my_select = web.element('//*[id="mySelect"]')
type(my_select)
```

```python title="Saída"
fastrpa.core.elements.SelectElement
```

### Tentando obter um `SelectElement`

```python linenums="1"
my_select = web.select('//*[id="mySelect"]')
type(my_select)
```

```python title="Saída"
fastrpa.core.elements.SelectElement
```

## Referência

### Obter todas as opções do select

```python linenums="1"
my_select.options
```

```python title="Saída"
{'1': 'Option 1',
 '2': 'Option 2'}
```

### Obter apenas os valores das opções

```python linenums="1"
my_select.options_values
```

```python title="Saída"
['1', '2']
```

### Obter apenas os rótulos das opções

```python linenums="1"
my_select.options_labels
```

```python title="Saída"
['Option 1', 'Option 2']
```

### Selecionar a opção pelo rótulo

```python linenums="1"
my_select.select('Option 1')
```

### Selecionar a opção pelo valor

```python linenums="1"
my_select.select(value='1')
```

### Obter o valor atual do select

```python linenums="1"
my_select.current
```

```python title="Saída"
('1', 'Option 1')
```

### Verificar se uma opção existe, por rótulo e valor

```python linenums="1"
'Option 3' in my_select
```

```python title="Saída"
False
```

### Verificar se uma opção existe, apenas pelo rótulo

```python linenums="1"
my_select.has_option('Option 3')
```

```python title="Saída"
False
```

### Verificar se uma opção existe, apenas pelo valor

```python linenums="1"
my_select.has_option(value='3')
```

```python title="Saída"
False
```

### Imprimir as opções do select

!!! warning "Extra necessário!"
    Para usar este método, você precisa instalar os extras **debug**, como [mostrado aqui](../index.md#installation), com o comando `pip install "fastrpa[debug]"`.

```python linenums="1"
my_select.print()
```

```python title="Saída"
[@id="mySelect"]
├── [1] Option 1
├── [2] Option 2
├── [3] Option 3
└── [4] Option 4
```
