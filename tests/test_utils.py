from fastrpa import utils
from selenium.webdriver import FirefoxOptions, ChromeOptions
from unittest.mock import MagicMock


def test_get_browser_options_default_options_class():
    options = utils.get_browser_options(['a', 'b'])
    assert type(options) is ChromeOptions
    assert options.arguments == ['a', 'b']


def test_get_browser_options():
    options = utils.get_browser_options(['a', 'b'], FirefoxOptions)
    assert type(options) is FirefoxOptions
    assert options.arguments == ['a', 'b']


def test_get_session():
    cookies_mock = [
        {
            'name': 'test',
            'value': 'test_value',
            'domain': 'www.site.com',
            'path': '/',
            'secure': False,
        }
    ]
    webdriver_mock = MagicMock(get_cookies=MagicMock(return_value=cookies_mock))
    session = utils.get_session(webdriver_mock)
    assert len(session.cookies) == 1
    assert session.cookies.get('test') == 'test_value'


def test_get_domain():
    webdriver_mock = MagicMock(current_url='https://www.site.com/')
    assert utils.get_domain(webdriver_mock) == 'www.site.com'
