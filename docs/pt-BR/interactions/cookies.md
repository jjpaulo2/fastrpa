---
description: Aprenda a gerenciar facilmente cookies no domínio atual.
---

Uma abstração para gerenciar cookies no domínio atual.

## Acessando o objeto

```python linenums="1"
app = FastRPA()
web = app.browse('https:...')
type(web.cookies)
```

```python title="Saída"
fastrpa.core.cookies.Cookies
```

## Referência

### Obter a lista de cookies no domínio atual

```python linenums="1"
web.cookies.list
```

```python title="Saída"
[Cookie(...), Cookie(...)]
```

### Obter a lista de nomes dos cookies no domínio atual

```python linenums="1"
web.cookies.list_names
```

```python title="Saída"
['JSESSIONID', '_ga', ...]
```

### Verificar se um cookie existe no domínio atual

```python linenums="1"
'my_cookie' in web.cookies
```

```python title="Saída"
True
```

### Verificar se um cookie armazena um determinado valor

```python linenums="1"
web.cookies.check('my_cookie', 'value')
```

```python title="Saída"
False
```

### Obter um cookie no domínio atual

```python linenums="1"
web.cookies.get('my_cookie')
```

```python title="Saída"
Cookie(name='...', value='...', domain='...', path='/', secure=True, http_only=True, same_site='Strict')
```

### Obter um cookie que não existe no domínio atual

```python linenums="1"
web.cookies.get('my_cookie')
```

```python title="Saída"
None
```

### Adicionar um novo cookie no domínio atual

```python linenums="1"
web.cookies.add('my_cookie', 'value')
```

```python title="Saída"
Cookie(name='my_cookie', value='value', domain='...', path='/', secure=False, http_only=True, same_site='Strict')
```

### Excluir um cookie no domínio atual

```python linenums="1"
web.cookies.delete('my_cookie')
```
