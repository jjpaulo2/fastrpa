---
description: Aprenda a enviar facilmente eventos de teclado para a página atual.
---

Você pode enviar eventos de teclado para a página atual usando os métodos abaixo.

## Acessando o objeto

```python linenums="1"
app = FastRPA()
web = app.browse('https:...')
type(web.keyboard)
```

```python title="Saída"
fastrpa.core.keyboard.Keyboard
```

## Referência

!!! info
    Todos os métodos de teclado são insensíveis a maiúsculas e minúsculas.

### Obter as teclas de comando disponíveis

```python linenums="1"
web.keyboard.keys
```

```python title="Saída"
['ADD',
 'ALT',
 'ARROW_DOWN',
 'ARROW_LEFT',
 'ARROW_RIGHT',
 'ARROW_UP',
 'BACKSPACE',
 'BACK_SPACE',
 ...
```

### Evento de pressionar tecla simples

```python linenums="1"
web.keyboard.press('control')
web.keyboard.press('escape')
web.keyboard.press('enter')
```

### Evento de atalho de teclado

```python linenums="1"
web.keyboard.shortcut('control', 'a')
web.keyboard.shortcut('control', 'shift', 'c')
```
