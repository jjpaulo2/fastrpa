---
title: Elementos
description: Aprenda a interagir facilmente com elementos da página.
---

# Elementos

!!! info "FastRPA é orientado a xpath!"

    FastRPA é totalmente baseado em **localizações xpath**. Isso significa que não existe outra forma, além do xpath, para acessar elementos nas páginas web. Este é um conceito importante que garante a consistência na base de código do framework.

    Se você deseja obter elementos usando outro identificador, basta escrever um xpath que encapsule esse identificador. Por exemplo, se você deseja obter um div com um id `my_div`, use o xpath `//*[@id="my_div"]`. Você pode usar um site como [xpather.com](http://xpather.com/) para ajudar a construir seus xpaths.

## Obter elementos da página

Para começar nossas interações com os elementos da página, precisamos apenas obtê-los com os métodos mostrados abaixo.

### Obter apenas um elemento ou o primeiro encontrado

```python linenums="1"
web.element('//*[@id="my_div"]')
```

```python title="Saída"
<fastrpa.core.elements.Element at 0x...>
```

#### A estratégia de espera

Por padrão, o FastRPA sempre espera até que o elemento seja interativo. O tempo limite padrão é de 15 segundos, e ele é configurável pelo construtor do FastRPA. Em caso de timeout, você receberá uma `ElementTimeoutException`.

```python linenums="1"
app = FastRPA(timeout=60)
web = app.browse('https:...')

# Se após o timeout, o elemento não estiver disponível
web.element('//*[@id="my_div"]')
```

```python title="Saída"
Traceback (most recent call last):
    ...
ElementTimeoutException: Elemento [//*[@id="my_div"]] não encontrado após 60 segundos!
```

#### Desativando a espera

Se você não quiser esperar, basta enviar o parâmetro `wait=False` para o método element.

```python linenums="1"
web.elements('//*[@id="my_div"]', wait=False)
```

```python title="Saída"
<fastrpa.core.elements.Element at 0x...>
```

Se você tentar obter um elemento que não está na página, você receberá uma `ElementNotFoundException`.

```python linenums="1"
web.elements('//*[@id="my_div"]', wait=False)
```

```python title="Saída"
Traceback (most recent call last):
    ...
ElementNotFoundException: Nenhum elemento [//*[@id="my_div"]] foi encontrado!
```

### Obter todos os elementos encontrados

```python linenums="1"
web.elements('//*[@id="my_div"]')
```

```python title="Saída"
[<fastrpa.core.elements.Element at 0x...>,
 <fastrpa.core.elements.Element at 0x...>]
```

No caso de tentar obter muitos elementos, o framework agora aplicará uma estratégia de espera.

```python linenums="1"
web.elements('//*[@id="my_inexistent_div"]')
```

```python title="Saída"
Traceback (most recent call last):
    ...
ElementNotFoundException: Nenhum elemento [//*[@id="my_div"]] foi encontrado!
```

## Abstrações de Elementos

Existem algumas abstrações que implementam ações e regras para elementos específicos. Elas estão listadas abaixo.

| Classe | Tags HTML5 |
|-|-|
| [`Element`](#element-reference) | qualquer elemento |
| [`InputElement`](./inputs.md) | `input`, `textarea` |
| [`FileInputElement`](./file-inputs.md) | `input type="file"` |
| [`RadioInputElement`](./radio-inputs.md) | `input type="radio"` |
| [`CheckboxElement`](./checkboxes.md) | `input type="checkbox"` |
| [`SelectElement`](./selects.md) | `select` |
| [`ListElement`](./lists.md) | `ol`, `ul` |
| [`ButtonElement`](./buttons.md) | `button`, `a` |
| [`FormElement`](./forms.md) | `form` |
| [`TableElement`](./tables.md) | `table` |
| [`ImageElement`](./images.md) | `img` |

## Referência de Elementos

Para interagir com instâncias genéricas de `Element`, você pode usar as propriedades e métodos abaixo.

### Obter o elemento

```python linenums="1"
element = web.element('//*[id="myElement"]')
type(element)
```

```python title="Saída"
fastrpa.core.elements.Element
```

### Obter a tag

```python linenums="1"
element.tag
```

```python title="Saída"
'div'
```

### Obter o id

```python linenums="1"
element.id
```

```python title="Saída"
'searchform'
```

### Obter as classes

```python linenums="1"
element.css_class
```

```python title="Saída"
['form', 'form-styled']
```

### Obter o CSS inline

```python linenums="1"
element.css_inline
```

```python title="Saída"
{'background-image': 'url("...")'}
```

### Obter o texto ou valor

```python linenums="1"
element.text
```

```python title="Saída"
'Fazer login'
```

### Retorna se o elemento é visível para o usuário

```python linenums="1"
element.is_visible
```

```python title="Saída"
True
```

### Retorna o valor para qualquer atributo do elemento, ou None se não existir

```python linenums="1"
element.attribute('data-property')
```

```python title="Saída"
'any value'
```

### Verifica se algum atributo possui um valor específico

```python linenums="1"
element.check('attribute', 'value')
```

```python title="Saída"
False
```

### Rolagem e movimento do cursor para o elemento

```python linenums="1"
element.focus()
```
