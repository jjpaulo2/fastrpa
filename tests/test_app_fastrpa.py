from unittest.mock import patch, MagicMock
from selenium.webdriver import ChromeOptions
from fastrpa import FastRPA


@patch('fastrpa.app.Remote')
def test_create_generical_instance_use_remote_webdriver(remote_mock: MagicMock):
    FastRPA().web()
    assert remote_mock.call_count == 1


@patch('fastrpa.app.Remote', MagicMock())
def test_get_generical_browser_options():
    options = FastRPA().browser_options
    assert type(options) is ChromeOptions
    assert options.arguments == ['--start-maximized', '--ignore-certificate-errors']
