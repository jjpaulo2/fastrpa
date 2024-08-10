---
description: Aprenda como esperar facilmente por alguns eventos.
---

Você pode esperar algum tempo antes ou depois de executar uma ação com a automação.

## Acessando o objeto

```python linenums="1"
app = FastRPA(timeout=60)
web = app.browse('https:...')
type(web.wait)
```

```python title="Saída"
fastrpa.core.wait.Wait
```

## Atalhos

### Esperar alguns segundos

O método é apenas um simples proxy para `time.sleep`, para remover a necessidade de uma importação adicional.

```python linenums="1"
web.wait.seconds(10)
```

## Referência

!!!info
    Por padrão, todos os métodos usam o **timeout** padrão da instância **FastRPA**. Todos os métodos listados abaixo aceitam um parâmetro final chamado **timeout** para especificar um valor personalizado.

### Esperar até que o elemento esteja presente

```python linenums="1"
web.wait.is_present('//button[@id="myBtn"]')
```

Para especificar um `timeout` personalizado, você pode fazer isso em qualquer método abaixo.

```python linenums="1"
web.wait.is_present('//button[@id="myBtn"]', 60)
web.wait.is_present('//button[@id="myBtn"]', timeout=60)
```

### Esperar até que o elemento **não** esteja presente

```python linenums="1"
web.wait.not_is_present('//button[@id="myBtn"]')
```

### Esperar até que o elemento seja clicável

```python linenums="1"
web.wait.is_clickable('//button[@id="myBtn"]')
```

### Esperar até que o elemento **não** seja clicável

```python linenums="1"
web.wait.not_is_clickable('//button[@id="myBtn"]')
```

### Esperar até que o elemento esteja oculto

```python linenums="1"
web.wait.is_hidden('//button[@id="myBtn"]')
```

### Esperar até que o elemento **não** esteja oculto

```python linenums="1"
web.wait.not_is_hidden('//button[@id="myBtn"]')
```

### Esperar até que o elemento contenha texto

```python linenums="1"
web.wait.contains_text('//button[@id="myBtn"]', 'qualquer texto')
```

### Esperar até que o elemento **não** contenha texto

```python linenums="1"
web.wait.not_contains_text('//button[@id="myBtn"]', 'qualquer texto')
```

### Esperar até que a URL contenha algum texto

```python linenums="1"
web.wait.url_contains('mysite.com/mypath')
```

### Esperar até que a URL **não** contenha algum texto

```python linenums="1"
web.wait.not_url_contains('mysite.com/mypath')
```

### Esperar até que o título contenha algum texto

```python linenums="1"
web.wait.title_contains('minha página')
```

### Esperar até que o título **não** contenha algum texto

```python linenums="1"
web.wait.not_title_contains('minha página')
```
