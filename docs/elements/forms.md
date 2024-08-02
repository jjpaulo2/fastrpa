---
description: Interactions with <form> tag.
---

Interactions with `form` tag.

## Reading the element

### Getting the right element class for the xpath

```python linenums="1"
my_form = web.element('//*[id="myForm"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.FormElement
```
### Try to get a `FormElement`

```python linenums="1"
my_form = web.button('//*[id="myForm"]')
type(my_select)
```

```python title="Output"
fastrpa.core.elements.FormElement
```

## Reference

### Get form method

```python linenums="1"
my_form.method
```

```python title="Output"
'POST'
```

### Get form action

```python linenums="1"
my_form.action
```

```python title="Output"
'https://www.mysite.com/form'
```

### Get form type

```python linenums="1"
my_form.type
```

```python title="Output"
'application/x-www-form-urlencoded'
```

### Submit the form

```python linenums="1"
my_form.submit()
```

### Submit the form by clicking in a button

```python linenums="1"
my_form.submit('//*[id="formSubmit"]')
```

## Success conditions

Forms also accept success conditions to ensure your form was properly filled. If any condition fail, the form raises a `FormException`.

### Set success by rediret to any url

```python linenums="1"
my_form.set_success_condition(redirect_url='https:://.../success_page.html')
```

### Set success by any element on the page

```python linenums="1"
my_form.set_success_condition(elements_to_find=['//div[@id="success_message"]'])
```

### Set success by any text on the page

```python linenums="1"
my_form.set_success_condition(text_to_find=['Success!'])
```

### Set success by all available conditions

```python linenums="1"
my_form.set_success_condition(
    redirect_url='https:://.../success_page.html',
    elements_to_find=['//div[@id="success_message"]'],
    text_to_find=['Success!'])
```

### Submit a form successfully

```python linenums="1"
my_form.submit()
```

### Fails a form submission

```python linenums="1"
my_form.submit()
```

```python title="Output"
Traceback (most recent call last):
    ...
FormException: The form submission got an error! Condition [redirect_url, https://...] not satisfied!
```