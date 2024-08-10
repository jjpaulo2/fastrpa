---
descrição: Interações com tags de botão e `a`.
---

Interações com tags `button` e `a`.

## Lendo o elemento

### Obtendo a classe de elemento correta para o xpath

```python linenums="1"
my_button = web.element('//*[id="myButton"]')
type(my_button)
```

```python title="Saída"
fastrpa.core.elements.ButtonElement
```

### Tentando obter um `ButtonElement`

```python linenums="1"
my_button = web.button('//*[id="myButton"]')
type(my_button)
```

```python title="Saída"
fastrpa.core.elements.ButtonElement
```

## Referência

### Verificar se o botão é um link

```python linenums="1"
my_button.is_link
```

```python title="Saída"
True
```

### Obter a referência do link

```python linenums="1"
my_button.reference
```

```python title="Saída"
'https://www.mysite.com/page'
```

### Realizar um duplo clique no botão

```python linenums="1"
my_button.double_click()
```
