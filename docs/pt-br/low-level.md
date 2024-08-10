---
description: Aprenda como acessar facilmente os objetos nativos do Selenium e do requests.
---

Nesta página, você aprenderá a acessar diretamente os objetos selenium e requests para implementar suas próprias abstrações, caso o FastRPA não ofereça algum recurso desejado.

## Obter instâncias de `WebDriver`

Tanto `FastRPA` quanto `Web` têm uma propriedade `webdriver` que sempre retorna uma instância de `WebDriver`. Um exemplo abaixo mostra o acesso ao objeto a partir da instância do `FastRPA`.

```python linenums="1"
app = FastRPA()
app.webdriver
```

```python title="Output"
<selenium.webdriver.remote.webdriver.WebDriver (session="...")>
```

Agora, para acessar o objeto a partir da instância do `Web`.

```python linenums="1"
web = app.web()
web.webdriver
```

```python title="Output"
<selenium.webdriver.remote.webdriver.WebDriver (session="...")>
```

## Obter instâncias de `WebElement`

Toda instância de `Element` tem uma propriedade `source` que sempre deve retornar uma instância de `WebElement`.

```python linenums="1"
element = web.element('//*[@id="myElement"]')
element.source
```

```python title="Output"
<selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>
```

## Obter instâncias de `Session`

O objeto `Web` tem uma propriedade `session`, que sempre retorna um objeto `Session` do requests. A sessão vem com todos os cookies da instância do webdriver.

```python linenums="1"
web = app.web()
web.session
```

```python title="Output"
<requests.sessions.Session at 0x1099352d0>
```
