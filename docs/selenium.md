---
description: Learn how to configurate a Selenium connection.
---

FastRPA needs a webdriver to work. It can be local, or remote. It's recommended to always use remote sessions.

## Injecting Selenium settings in FastRPA

By default, FastRPA always connect to `http://localhost:4444`. If you want to change it, just create your own Selenium instance.

### Custom Selenium instance

```python linenums="1"
from fastrpa import FastRPA
from selenium.webdriver import Firefox, FirefoxOptions

options = FirefoxOptions()
firefox = Firefox(options, keep_alive=False)
fastrpa = FastRPA(firefox)
```

!!! warning
    Use local webdrives only for debugging purpose. For production, the best way is always use a containerized instance.

### Customize only browser options

By default, FastRPA uses just the parameters `--start-maximized` and `--ignore-certificate-errors`. But you can easier customize it.

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

FastRPA assumes you are running a Chromium session on `localhost:4444`. If you just want to change Chromium arguments, just send the `browser_arguments` parameter.

```python linenums="1"
from fastrpa import FastRPA

fastrpa = FastRPA(
    browser_arguments=[
        '--incognito',
        '--disable-notifications'
    ]
)
```

## Setup a Selenium container

You can run a remote session of webdriver using docker, as below. You must always expose the port `4444` for Selenium connection, and opcionaly, expose `7900` for noVNC connection to able you see the automation running.

!!! info
    You can access noVNC from [http://localhost:7900/?autoconnect=1&password=secret](http://localhost:7900/?autoconnect=1&password=secret).

### Setup Chromium

```shell
docker run -d \
    --name selenium-chromium \
    -p 4444:4444 \
    -p 7900:7900 \
    selenium/standalone-chromium:latest
```

### Setup Firefox

```shell
docker run -d \
    --name selenium \
    -p 4444:4444 \
    -p 7900:7900 \
    selenium/standalone-firefox:latest
```

### Setup Edge

```shell
docker run -d \
    --name selenium-edge \
    -p 4444:4444 \
    -p 7900:7900 \
    selenium/standalone-edge:latest
```
