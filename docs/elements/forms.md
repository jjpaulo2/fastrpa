Interactions with `form` tag.

## Reading the element

### Getting the right element class for the xpath

```python
>>> my_form = web.element('//*[id="myForm"]')
>>> type(my_select)
fastrpa.core.elements.FormElement
```
### Try to get a `FormElement`

```python
>>> my_form = web.button('//*[id="myForm"]')
>>> type(my_select)
fastrpa.core.elements.FormElement
```

## Reference

### Get form method

```python
>>> my_form.method
'POST'
```

### Get form action

```python
>>> my_form.action
'https://www.mysite.com/form'
```

### Get form type

```python
>>> my_form.type
'application/x-www-form-urlencoded'
```

### Submit the form

```python
>>> my_form.submit()
```

### Submit the form by clicking in a button

```python
>>> my_form.submit('//*[id="formSubmit"]')
```

## Success conditions

Forms also accept success conditions to ensure your form was properly filled. If any condition fail, the form raises a `FormException`.

### Set success by rediret to any url

```python
>>> my_form.set_success_condition(redirect_url='https:://.../success_page.html')
```

### Set success by any element on the page

```python
>>> my_form.set_success_condition(elements_to_find=['//div[@id="success_message"]'])
```

### Set success by any text on the page

```python
>>> my_form.set_success_condition(text_to_find=['Success!'])
```

### Set success by all available conditions

```python
>>> my_form.set_success_condition(
    redirect_url='https:://.../success_page.html',
    elements_to_find=['//div[@id="success_message"]'],
    text_to_find=['Success!'])
```

### Submit a form successfully

```python
>>> my_form.submit()
```

### Fails a form submission

```python
>>> my_form.submit()
Traceback (most recent call last):
    ...
FormException: The form submission got an error! Condition [redirect_url, https://...] not satisfied!
```