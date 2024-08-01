# FastRPA

[![Tests](https://github.com/jjpaulo2/fastrpa/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/jjpaulo2/fastrpa/actions/workflows/tests.yaml)
![Python](https://img.shields.io/badge/Python-3.10_%7C_3.11_%7C_3.12-green)
![PyPI - Version](https://img.shields.io/pypi/v/fastrpa)

A simple to use abstraction over Selenium.


## Installation

To perform a basic installation, just run:

```
pip install fastrpa
```

To install also, packages to help you to debug your application, install with **\[debug\]** extras:

```
pip install fastrpa[debug]
```

## Your first instance

The FastRPA object, will prepare everything you need to start browse on the web. You can pass Selenium configurations to it. See [here](./selenium.md) how to do it.

```python
>>> from fastrpa import FastRPA
>>> app = FastRPA()
>>> web = app.browse('https:...')
>>> type(web)
fastrpa.app.Web
```
