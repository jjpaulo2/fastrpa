---
título: Documentação
descrição: Documentação oficial do FastRPA. Uma abstração simples sobre o Selenium.
---

# FastRPA

![Python](https://img.shields.io/badge/Python-3.10_%7C_3.11_%7C_3.12-green)
[![Tests](https://github.com/jjpaulo2/fastrpa/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/jjpaulo2/fastrpa/actions/workflows/tests.yaml)
[![Documentation](https://github.com/jjpaulo2/fastrpa/actions/workflows/docs.yaml/badge.svg?branch=main)](https://github.com/jjpaulo2/fastrpa/actions/workflows/docs.yaml)
[![Publish](https://github.com/jjpaulo2/fastrpa/actions/workflows/publish.yaml/badge.svg)](https://github.com/jjpaulo2/fastrpa/actions/workflows/publish.yaml)
[![PyPI - Version](https://img.shields.io/pypi/v/fastrpa)](https://pypi.org/project/fastrpa/)
[![Sponsor](https://img.shields.io/badge/Sponsor-FastRPA-deeppink)](https://github.com/sponsors/jjpaulo2)

Uma abstração simples sobre o Selenium.

- [x] **Fácil de usar**: interações complexas são abstraídas para métodos intuitivos.
- [x] **Imports limpos**: elimina a necessidade de importar muitos pacotes e objetos. Todos os recursos de automação são acessíveis por métodos de um único objeto principal.
- [x] **Tipado**: dicas de tipo garantem a legibilidade do código e tornam possível navegar pelos métodos com qualquer ferramenta de Intellisense.
- [x] **Seguro para Selenium**: o núcleo foi desenvolvido seguindo as melhores práticas do Selenium. Você pode se concentrar nas regras de negócios.

# Instalação

Para uma instalação básica, execute:

```
pip install fastrpa
```

Para instalar também pacotes que ajudam a depurar sua aplicação, instale com o extra **debug**:

```
pip install "fastrpa[debug]"
```

## Sua primeira instância

O objeto FastRPA preparará tudo o que você precisa para começar a navegar na web. Você pode passar configurações do Selenium para ele. Veja [aqui](./selenium.md) como fazer isso.

```python linenums="1"
from fastrpa import FastRPA
app = FastRPA()
web = app.web()
type(web)
```

```python title="Saída"
fastrpa.app.Web
```

Você também pode instanciar um objeto Web e navegar para uma URL inicial.

```python linenums="1"
web = app.web('https://...')
```

## Os objetos Web

Uma vez que você tem um objeto `Web`, você pode navegar na web. A classe `Web` é uma abstração das principais funções do navegador e do usuário.

### Obter a URL atual do navegador

```python linenums="1"
web.url
```

```python title="Saída"
'https://www.site.com/mypage'
```

### Obter o domínio da URL atual

```python linenums="1"
web.domain
```

```python title="Saída"
'www.site.com'
```

### Obter o título da página atual

```python linenums="1"
web.title
```

```python title="Saída"
'Meu site'
```

### Obter o código-fonte HTML da página atual

```python linenums="1"
web.html
```

```python title="Saída"
'<html lang="en"><head>\n    <meta charset="utf-8">...'
```

### Navegar para uma URL

```python linenums="1"
web.browse('https://www.site.com/another_page')
```

### Atualizar a página atual

```python linenums="1"
web.refresh()
```

### Verificar se um elemento está interativo na tela

```python linenums="1"
web.is_interactive('//*[@id="myElement"]')
```

```python title="Saída"
False
```

### Obter o conteúdo de texto de um elemento

```python linenums="1"
web.read('//*[@id="myElement"]')
```

```python title="Saída"
'Qualquer texto'
```

## Próximos passos

- [Configurar a integração com o selenium](./selenium.md)
- [Executar interações com a página atual](./interactions/index.md)
- [Manipular elementos](./elements/index.md)
- [Obter xpaths de forma mais fácil](./xpath-tools.md)
- [Usar a API selenium/requests diretamente](./low-level.md)
