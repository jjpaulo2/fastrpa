---
description: Interactions with input tag with attribute [@type="radio"].
---

Interactions with `input` with attribute `type="radio"`.

## Reading the element

### Getting the right element class for the xpath

```python linenums="1"
my_radio = web.radio_input('//*[id="myRadioInput"]')
type(my_radio)
```

```python title="Output"
fastrpa.core.elements.RadioInputElement
```

### Try to get a `RadioInputElement`

```python linenums="1"
my_radio = web.file_input('//*[id="myRadioInput"]')
type(my_radio)
```

```python title="Output"
fastrpa.core.elements.RadioInputElement
```

## Reference

### Get all radio options

Given one radio element, you can query by another options with same `@name` attribute. This method will returns a dict with radio values and it's respective label text associated.

```python linenums="1"
my_radio.options
```

```python title="Output"
{'option1': 'Default radio',
 'option2': 'Second default radio'}
```

### Get all radio options values

```python linenums="1"
my_radio.options_values
```

```python title="Output"
['option1', 'option2']
```

### Get all radio options labels

This method will return all texts from labels pointing to radio elements with same `@name` of the source radio element.

```python linenums="1"
my_radio.options_values
```

```python title="Output"
['Default radio', 'Second default radio']
```

### Select a radio option by label

Following the same rule, you can select another radio from the form with the same `@name` of the source radio element.

```python linenums="1"
my_radio.select('Second default radio')
```

### Select a radio option by value

```python linenums="1"
my_radio.select(value='option1')
```

### To just active the source radio element

```python linenums="1"
my_radio.click()
```

### Check if radios have some option

To check by both label and value.

```python linenums="1"
'Other option' in my_radio
```

```python title="Output"
False
```

### Check if radios have some option label

```python linenums="1"
my_radio.has_option('Other option')
```

```python title="Output"
False
```

### Check if radios have some option value

```python linenums="1"
my_radio.has_option(value='3')
```

```python title="Output"
False
```

### Print the options of the radio

!!! warning "Extra needed!"
    To use this method, you need to install the **debug** extras, as [shown here](../index.md#installation), with the command `pip install "fastrpa[debug]"`.

```python linenums="1"
my_radio.print()
```

```python title="Output"
[@id="myRadioInput"]
├── [1] Option 1
├── [2] Option 2
├── [3] Option 3
└── [4] Option 4
```