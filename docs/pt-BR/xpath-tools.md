---
description: Aprenda como gerar facilmente XPaths.
---

Para ajudar você a gerar XPaths facilmente, o FastRPA contém um submódulo `xpath`.

## Importação

```python linenums="1"
from fastrpa import xpath
```

## Atributos específicos

### Id contém valor

```python linenums="1"
xpath.id_contains('some-value')
```

```python title="Output"
'//*[contains(@id, "some-value")]'
```

Para gerar um XPath com elementos filhos, você pode usar um argumento `child` no final. Todas as funções abaixo permitem este argumento.

```python linenums="1"
xpath.id_contains('some-value', '/id/span')
```

```python title="Output"
'//*[contains(@id, "some-value")]/id/span'
```

### Id é igual ao valor

```python linenums="1"
xpath.id_equals('some-value')
```

```python title="Output"
'//*[@id="some-value"]'
```

### Classe contém valor

```python linenums="1"
xpath.class_contains('some-value')
```

```python title="Output"
'//*[contains(@class, "some-value")]'
```

### Classe é igual ao valor

```python linenums="1"
xpath.class_equals('some-value')
```

```python title="Output"
'//*[@class="some-value"]'
```

### Nome contém valor

```python linenums="1"
xpath.name_equals('some-value')
```

```python title="Output"
'//*[contains(@name, "some-value")]'
```

### Nome é igual ao valor

```python linenums="1"
xpath.id_equals('some-value')
```

```python title="Output"
'//*[@name="some-value"]'
```

### Texto contém valor

```python linenums="1"
xpath.text_contains('some-value')
```

```python title="Output"
'//*[contains(text(), "some-value")]'
```

### Texto é igual ao valor

```python linenums="1"
xpath.text_equals('some-value')
```

```python title="Output"
'//*[text()="some-value"]'
```

## Atributos genéricos

### Atributo de tag contém algum valor

```python linenums="1"
xpath.attribute_contains('div', '@id', 'value')
```

```python title="Output"
'//div[contains(@id, "value")]'
```

### Atributo de tag é igual a algum valor

```python linenums="1"
xpath.attribute_equals('div', '@id', 'value')
```

```python title="Output"
'//div[@id="value"]'
```
