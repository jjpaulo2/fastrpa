# FastRPA

A simple to use abstraction over Selenium.

### Installation

To perform a basic installation, just run:

```
pip install fastrpa
```

To install also, packages to help you to debug your application, install with **\[debug\]** extras:

```
pip install fastrpa[debug]
```

### How to use

For details, read the [documentation](./docs/index.md).

## For development

Make sure you have poetry installed and upgraded.

```shell
pip install --upgrade pip poetry
```

### Install dependencies

```shell
poetry install --with dev
```

### Project commands

| Command | Description |
|-|-|
| `poetry build` | Build the project |
| `poetry run task tests` | Runs all unit tests |
| `poetry run task lint` | Format and lint the code |
| `poetry run task security` | Check security issues on the code |
| `poetry run task check` | Check code issues |
