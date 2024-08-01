Interactions with `form` tag.

```python
# Gets the right element class for the xpath
>>> my_form = web.element('//*[id="myForm"]')
>>> type(my_select)
fastrpa.core.elements.FormElement

# Try to get a FormElement
>>> my_form = web.button('//*[id="myForm"]')
>>> type(my_select)
fastrpa.core.elements.FormElement

# Get form method
>>> my_form.method
'POST'

# Get form action
>>> my_form.action
'https://www.mysite.com/form'

# Get form type
>>> my_form.type
'application/x-www-form-urlencoded'

# Submit the form
>>> my_form.submit()

# Submit the form by clicking in a button
>>> my_form_button = web.button('//*[id="formSubmit"]')
>>> my_form.submit(my_form_button)
```

Forms also accept success conditions to ensure your form was properly filled. If any condition fail, the form raises a `FormException`.

```python
# Set success by redireto to any url
>>> my_form.set_success_condition(redirect_url='https:://.../success_page.html')

# Set success by any element on the page
>>> my_form.set_success_condition(elements_to_find=['//div[@id="success_message"]'])

# Set success by any text on the page
>>> my_form.set_success_condition(text_to_find=['Success!'])

# Set success by all available conditions
>>> my_form.set_success_condition(
    redirect_url='https:://.../success_page.html',
    elements_to_find=['//div[@id="success_message"]'],
    text_to_find=['Success!'])

# Submit a form successfully
>>> my_form.submit()

# Fails a form submission
>>> my_form.submit()
Traceback (most recent call last):
    ...
FormException: The form submission got an error! Condition [redirect_url, https://...] not satisfied!
```