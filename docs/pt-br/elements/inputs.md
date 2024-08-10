---
description: Interações com tags `input` e `textarea`.
---

Interações com tags `input` e `textarea`.

## Lendo o elemento

### Obtendo a classe correta do elemento para o xpath

```python linenums="1"
my_input = web.element('//*[id="myInput"]')
type(my_input)
```

```python title="Saída"
fastrpa.core.elements.InputElement
```

### Tentando obter um `InputElement`

```python linenums="1"
my_input = web.input('//*[id="myInput"]')
type(my_input)
```

```python title="Saída"
fastrpa.core.elements.InputElement
```

## Referência

### Limpar o valor do elemento

```python linenums="1"
my_input.clear()
```

### Preencher a caixa de entrada com um valor

```python linenums="1"
my_input.fill('my input')
```

### Preencher a caixa de entrada, tecla por tecla

```python linenums="1"
my_input.fill_slowly('my input')

# Preencher a caixa de entrada, tecla por tecla, aguardando 3 segundos entre cada tecla enviada
my_input.fill_slowly('my input', 3)
```
