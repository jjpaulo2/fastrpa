---
description: Aprenda a executar JavaScript facilmente na página atual.
---

Para executar JavaScript na página atual, você pode usar os seguintes métodos.

## Acessando o objeto

```python linenums="1"
app = FastRPA()
web = app.browse('https:...')
type(web.console)
```

```python title="Saída"
fastrpa.core.console.Console
```

## Referência

### Avaliar uma expressão simples

```python linenums="1"
web.console.evaluate('2 + 2')
```

```python title="Saída"
4
```

### Executar scripts de várias linhas

```python linenums="1"
web.console.run([
    'button = document.getElementById("myButton")',
    'button.click()'
])
```

### Executar um arquivo JavaScript

```python linenums="1"
web.console.run_script('/caminho/para/script.js')
```
