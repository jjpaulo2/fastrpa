---
description: Interações com a tag `form`.
---

Interações com a tag `form`.

## Lendo o elemento

### Obtendo a classe de elemento correta para o xpath

```python linenums="1"
my_form = web.element('//*[id="myForm"]')
type(my_select)
```

```python title="Saída"
fastrpa.core.elements.FormElement
```

### Tentando obter um `FormElement`

```python linenums="1"
my_form = web.button('//*[id="myForm"]')
type(my_select)
```

```python title="Saída"
fastrpa.core.elements.FormElement
```

## Referência

### Obter o método do formulário

```python linenums="1"
my_form.method
```

```python title="Saída"
'POST'
```

### Obter a ação do formulário

```python linenums="1"
my_form.action
```

```python title="Saída"
'https://www.mysite.com/form'
```

### Obter o tipo do formulário

```python linenums="1"
my_form.type
```

```python title="Saída"
'application/x-www-form-urlencoded'
```

### Enviar o formulário

```python linenums="1"
my_form.submit()
```

### Enviar o formulário clicando em um botão

```python linenums="1"
my_form.submit('//*[id="formSubmit"]')
```

## Condições de sucesso

Os formulários também aceitam condições de sucesso para garantir que seu formulário foi preenchido corretamente. Se alguma condição falhar, o formulário gera uma `FormException`.

### Definir sucesso por redirecionamento para qualquer URL

```python linenums="1"
my_form.set_success_condition(redirect_url='https:://.../success_page.html')
```

### Definir sucesso por qualquer elemento na página

```python linenums="1"
my_form.set_success_condition(elements_to_find=['//div[@id="success_message"]'])
```

### Definir sucesso por qualquer texto na página

```python linenums="1"
my_form.set_success_condition(text_to_find=['Success!'])
```

### Definir sucesso por todas as condições disponíveis

```python linenums="1"
my_form.set_success_condition(
    redirect_url='https:://.../success_page.html',
    elements_to_find=['//div[@id="success_message"]'],
    text_to_find=['Success!'])
```

### Enviar um formulário com sucesso

```python linenums="1"
my_form.submit()
```

### Falhar na submissão de um formulário

```python linenums="1"
my_form.submit()
```

```python title="Saída"
Traceback (most recent call last):
    ...
FormException: A submissão do formulário encontrou um erro! Condição [redirect_url, https://...] não satisfeita!
```
