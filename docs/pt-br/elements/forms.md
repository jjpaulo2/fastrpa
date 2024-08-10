---
descrição: Interações com a tag `img`.
---

Interações com a tag `img`.

## Lendo o elemento

### Obtendo a classe de elemento correta para o xpath

```python linenums="1"
my_image = web.element('//*[id="myImage"]')
type(my_image)
```

```python title="Saída"
fastrpa.core.elements.ImageElement
```

### Tentando obter um `ImageElement`

```python linenums="1"
my_image = web.image('//*[id="myImage"]')
type(my_image)
```

```python title="Saída"
fastrpa.core.elements.ImageElement
```

## Referência

### Obter o caminho da imagem do atributo src

```python linenums="1"
my_image.reference
```

```python title="Saída"
'https://mysite.com/resources/image.png'
```

### Obter o texto alternativo do atributo alt

```python linenums="1"
my_image.text
```

```python title="Saída"
'Uma imagem do site'
```

### Salvar a imagem no diretório de trabalho atual

```python linenums="1"
my_image.save()
```

### Salvar a imagem em um caminho personalizado

```python linenums="1"
my_image.save('/my/path/image.png')
```
