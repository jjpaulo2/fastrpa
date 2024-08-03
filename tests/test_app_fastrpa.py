from unittest.mock import patch, MagicMock
from selenium.webdriver import ChromeOptions, FirefoxOptions
from fastrpa import FastRPA
from fastrpa.app import Web


@patch('fastrpa.app.Remote')
def test_generical_instance_use_remote_webdriver(remote_mock: MagicMock):
    FastRPA().web()
    assert remote_mock.call_count == 1


@patch('fastrpa.app.Remote', MagicMock())
def test_get_generical_browser_options():
    options = FastRPA().browser_options
    assert type(options) is ChromeOptions
    assert options.arguments == [
        '--start-maximized',
        '--ignore-certificate-errors',
    ]


@patch('fastrpa.app.Remote', MagicMock())
def test_get_specific_browser_options_class():
    fastrpa = FastRPA(options_class=FirefoxOptions)
    options = fastrpa.browser_options
    assert type(options) is FirefoxOptions
    assert options.arguments == [
        '--start-maximized',
        '--ignore-certificate-errors',
    ]


@patch('fastrpa.app.Remote', MagicMock())
def test_get_specific_browser_arguments():
    fastrpa = FastRPA(browser_arguments=['arg1', 'arg2'])
    options = fastrpa.browser_options
    assert type(options) is ChromeOptions
    assert options.arguments == ['arg1', 'arg2']


@patch('fastrpa.app.Remote', MagicMock())
def test_get_specific_browser_arguments_and_options_class():
    fastrpa = FastRPA(
        options_class=FirefoxOptions, browser_arguments=['arg1', 'arg2']
    )
    options = fastrpa.browser_options
    assert type(options) is FirefoxOptions
    assert options.arguments == ['arg1', 'arg2']


@patch('fastrpa.app.Remote')
def test_webdriver_is_quitting(remote_mock: MagicMock):
    quit_mock = MagicMock()
    remote_mock.return_value = MagicMock(quit=quit_mock)
    fastrpa = FastRPA()
    del fastrpa
    assert quit_mock.call_count == 1


@patch('fastrpa.app.Remote', MagicMock())
def test_get_web_instance():
    fastrpa = FastRPA(timeout=99)
    web = fastrpa.web()
    assert type(web) is Web
    assert web.timeout == 99


@patch('fastrpa.app.Remote', MagicMock())
@patch('fastrpa.app.Web')
def test_get_web_instance_and_browse(web_mock: MagicMock):
    browse_mock = MagicMock()
    web_mock.return_value = MagicMock(browse=browse_mock)
    FastRPA().web('some-url')
    assert browse_mock.call_count == 1
    assert browse_mock.call_args.args == ('some-url',)
