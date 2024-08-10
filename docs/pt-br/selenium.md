---
description: Aprenda como configurar uma conexão Selenium.
---

O FastRPA precisa de um webdriver para funcionar. Pode ser local ou remoto. É recomendado sempre usar sessões remotas.

## Injetando configurações Selenium no FastRPA

Por padrão, o FastRPA sempre se conecta a `http://localhost:4444`. Se você quiser alterar isso, basta criar sua própria instância Selenium.

### Instância Selenium personalizada

```python linenums="1"
from fastrpa import FastRPA
from selenium.webdriver import Firefox, FirefoxOptions

options = FirefoxOptions()
firefox = Firefox(options, keep_alive=False)
fastrpa = FastRPA(firefox)
```

!!! warning
    Use webdrivers locais apenas para fins de depuração. Para produção, a melhor forma é sempre usar uma instância containerizada.

### Personalizar apenas opções do navegador

Por padrão, o FastRPA usa apenas os parâmetros `--start-maximized` e `--ignore-certificate-errors`. Mas você pode personalizar mais facilmente.

```python linenums="1"
from fastrpa import FastRPA
from selenium.webdriver import ChromeOptions

fastrpa = FastRPA(
    options_class=ChromeOptions,
    browser_arguments=[
        '--incognito',
        '--disable-notifications'
    ]
)
```

O FastRPA assume que você está executando uma sessão Chromium em `localhost:4444`. Se você só quiser alterar os argumentos do Chromium, basta enviar o parâmetro `browser_arguments`.

```python linenums="1"
from fastrpa import FastRPA

fastrpa = FastRPA(
    browser_arguments=[
        '--incognito',
        '--disable-notifications'
    ]
)
```

## Configurar um container Selenium

Você pode executar uma sessão remota de webdriver usando o docker, conforme abaixo. Você deve sempre expor a porta `4444` para a conexão Selenium e, opcionalmente, expor `7900` para a conexão noVNC para permitir visualizar a automação em execução.

!!! info
    Você pode acessar o noVNC em [http://localhost:7900/?autoconnect=1&password=secret](http://localhost:7900/?autoconnect=1&password=secret).

### Configurar Chromium

```shell
docker run -d \
    --name selenium-chromium \
    -p 4444:4444 \
    -p 7900:7900 \
    selenium/standalone-chromium:latest
```

### Configurar Firefox

```shell
docker run -d \
    --name selenium \
    -p 4444:4444 \
    -p 7900:7900 \
    selenium/standalone-firefox:latest
```

### Configurar Edge

```shell
docker run -d \
    --name selenium-edge \
    -p 4444:4444 \
    -p 7900:7900 \
    selenium/standalone-edge:latest
```
