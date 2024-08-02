---
description: Learn how to easily generate xpaths.
---

To help you generate easy xpaths, FastRPA contains a submodule `xpath`.

## Importing

```python linenums="1"
from fastrpa import xpath
```

## Specific attributes

### Id contains value

```python linenums="1"
xpath.id_contains('some-value')
```

```python title="Output"
'//*[contains(@id, "some-value")]'
```

To generate a xpath with children elements, you can use a last `child` argument. All funcions below allows this argument.

```python linenums="1"
xpath.id_contains('some-value', '/id/span')
```

```python title="Output"
'//*[contains(@id, "some-value")]/id/span'
```

### Id equals to value

```python linenums="1"
xpath.id_equals('some-value')
```

```python title="Output"
'//*[@id="some-value"]'
```

### Class contains value

```python linenums="1"
xpath.class_contains('some-value')
```

```python title="Output"
'//*[contains(@class, "some-value")]'
```

### Class equals to value

```python linenums="1"
xpath.class_equals('some-value')
```

```python title="Output"
'//*[@class="some-value"]'
```

### Name contains value

```python linenums="1"
xpath.name_equals('some-value')
```

```python title="Output"
'//*[contains(@name, "some-value")]'
```

### Name equals to value

```python linenums="1"
xpath.id_equals('some-value')
```

```python title="Output"
'//*[@name="some-value"]'
```

### Text contains value

```python linenums="1"
xpath.text_contains('some-value')
```

```python title="Output"
'//*[contains(text(), "some-value")]'
```

### Text equals to value

```python linenums="1"
xpath.text_equals('some-value')
```

```python title="Output"
'//*[text()="some-value"]'
```

## Generical attributes

### Tag attribute contains some value

```python linenums="1"
xpath.attribute_contains('div', '@id', 'value')
```

```python title="Output"
'//div[contains(@id, "value")]'
```

### Tag attribute equals to some value

```python linenums="1"
xpath.attribute_equals('div', '@id', 'value')
```

```python title="Output"
'//div[@id="value"]'
```