---
description: Interações com a tag `input` com atributo [@type="checkbox"].
---

Interações com `input` com atributo `type="checkbox"`.

## Lendo o elemento

### Obtendo a classe de elemento correta para o xpath

```python linenums="1"
my_check = web.checkbox('//*[id="myCheckbox"]')
type(my_check)
```

```python title="Saída"
fastrpa.core.elements.CheckboxElement
```

### Tentando obter um `CheckboxElement`

```python linenums="1"
my_check = web.checkbox('//*[id="myCheckbox"]')
type(my_check)
```

```python title="Saída"
fastrpa.core.elements.CheckboxElement
```

## Referência

### Verificar se está marcado

```python linenums="1"
my_check.is_checked
```

```python title="Saída"
False
```

### Marcar como selecionado

Apenas marca a caixa de seleção como ativa.

```python linenums="1"
my_check.check()
```

### Desmarcar

Apenas desmarca a caixa de seleção como inativa.

```python linenums="1"
my_check.uncheck()
```

### Alternar o valor

Apenas alterna o valor da caixa de seleção. Se estiver marcada, será desmarcada, e vice-versa.

```python linenums="1"
my_check.switch()
```
