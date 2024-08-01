FastRPA needs a webdriver to work. It can be local, or remote. It's recommended to always use remote sessions.

You can run a remote session of Chromium webdriver using docker, as below.

```shell
# For x86 machines
docker run --name selenium -d -p 4444:4444 -p 7900:7900 selenium/standalone-chromium:latest

# For ARM machines
docker run --name selenium -d -p 4444:4444 -p 7900:7900 seleniarm/standalone-chromium:latest
```

By default, FastRPA always connect to `http://localhost:4444`. If you want to change it, just create your own Selenium instance.

```python linenums="1"
from fastrpa import FastRPA
from selenium.webdriver import Firefox, FirefoxOptions

options = FirefoxOptions()
options.add_argument(...)
options.add_argument(...)

webdriver = Firefox(options)
app = FastRPA(webdriver)
```
