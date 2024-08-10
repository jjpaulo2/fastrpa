---
description: Aprenda a gerenciar e navegar facilmente pelas abas do navegador.
---

Para gerenciar e navegar pelas abas do navegador, use os seguintes métodos.

## Acessando o objeto

```python linenums="1"
app = FastRPA()
web = app.browse('https:...')
type(web.tabs)
```

```python title="Saída"
fastrpa.core.tabs.Tabs
```

## Referência

### Obter abas abertas

```python linenums="1"
web.tabs.list
```

```python title="Saída"
['AD9B396BF70C366D8A1FDE5450699D41', ...]
```

### Obter a aba atual

```python linenums="1"
web.tabs.current
```

```python title="Saída"
'AD9B396BF70C366D8A1FDE5450699D41'
```

### Obter o índice da aba atual

```python linenums="1"
web.tabs.current_index
```

```python title="Saída"
0
```

### Obter a contagem de abas abertas

```python linenums="1"
len(web.tabs)
```

```python title="Saída"
5
```

### Abrir uma nova aba

Este método também muda para a nova aba e retorna o id da nova aba.

```python linenums="1"
web.tabs.new()
```

```python title="Saída"
'AD9B396BF70C366D8A1FDE5450699D41'
```

### Fechar a aba atual

```python linenums="1"
web.tabs.close()
```

### Verificar se uma aba está aberta

```python linenums="1"
'AD9B396BF70C366D8A1FDE5450699D41' in web.tabs
```

```python title="Saída"
True
```
