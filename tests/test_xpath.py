from fastrpa import xpath
from pytest import mark


@mark.parametrize(
    ('element', 'attribute', 'value', 'child', 'expected_output'),
    (
        ('div', '@id', 'someValue', '', '//div[contains(@id, "someValue")]'),
        ('a', '@class', 'someValue', '/i', '//a[contains(@class, "someValue")]/i'),
        ('*', 'data-value', 'someValue', '/i/div', '//*[contains(data-value, "someValue")]/i/div'),
    ),
    ids=(
        '//div[contains(@id, "someValue")]',
        '//a[contains(@class, "someValue")]/i',
        '//*[contains(data-value, "someValue")]/i/div'
    )
)
def test_attribute_contains(element, attribute, value, child, expected_output):
    assert xpath.attribute_contains(element, attribute, value, child) == expected_output


@mark.parametrize(
    ('element', 'attribute', 'value', 'child', 'expected_output'),
    (
        ('div', '@id', 'someValue', '', '//div[@id="someValue"]'),
        ('a', '@class', 'someValue', '/i', '//a[@class="someValue"]/i'),
        ('*', 'data-value', 'someValue', '/i/div', '//*[data-value="someValue"]/i/div'),
    ),
    ids=(
        '//div[@id="someValue"]',
        '//a[@class="someValue"]/i',
        '//*[data-value="someValue"]/i/div'
    )
)
def test_attribute_equals(element, attribute, value, child, expected_output):
    assert xpath.attribute_equals(element, attribute, value, child) == expected_output


@mark.parametrize(
    ('value', 'child', 'expected_output'),
    (
        ('someValue', '', '//*[contains(@id, "someValue")]'),
        ('some.value', '/i/div', '//*[contains(@id, "some.value")]/i/div'),
        ('some_value', '/i/div', '//*[contains(@id, "some_value")]/i/div'),
        ('some-value', '/i/div', '//*[contains(@id, "some-value")]/i/div'),
    ),
    ids=(
        '//*[contains(@id, "someValue")]',
        '//*[contains(@id, "some.value")]/i/div',
        '//*[contains(@id, "some_value")]/i/div',
        '//*[contains(@id, "some-value")]/i/div'
    )
)
def test_id_contains(value, child, expected_output):
    assert xpath.id_contains(value, child) == expected_output


@mark.parametrize(
    ('value', 'child', 'expected_output'),
    (
        ('someValue', '', '//*[@id="someValue"]'),
        ('some.value', '/i/div', '//*[@id="some.value"]/i/div'),
        ('some_value', '/i/div', '//*[@id="some_value"]/i/div'),
        ('some-value', '/i/div', '//*[@id="some-value"]/i/div'),
    ),
    ids=(
        '//*[@id="someValue"]',
        '//*[@id="some.value"]/i/div',
        '//*[@id="some_value"]/i/div',
        '//*[@id="some-value"]/i/div'
    )
)
def test_id_equals(value, child, expected_output):
    assert xpath.id_equals(value, child) == expected_output


@mark.parametrize(
    ('value', 'child', 'expected_output'),
    (
        ('someValue', '', '//*[contains(@class, "someValue")]'),
        ('some.value', '/i/div', '//*[contains(@class, "some.value")]/i/div'),
        ('some_value', '/i/div', '//*[contains(@class, "some_value")]/i/div'),
        ('some-value', '/i/div', '//*[contains(@class, "some-value")]/i/div'),
    ),
    ids=(
        '//*[contains(@class, "someValue")]',
        '//*[contains(@class, "some.value")]/i/div',
        '//*[contains(@class, "some_value")]/i/div',
        '//*[contains(@class, "some-value")]/i/div'
    )
)
def test_class_contains(value, child, expected_output):
    assert xpath.class_contains(value, child) == expected_output


@mark.parametrize(
    ('value', 'child', 'expected_output'),
    (
        ('someValue', '', '//*[@class="someValue"]'),
        ('some.value', '/i/div', '//*[@class="some.value"]/i/div'),
        ('some_value', '/i/div', '//*[@class="some_value"]/i/div'),
        ('some-value', '/i/div', '//*[@class="some-value"]/i/div'),
    ),
    ids=(
        '//*[@class="someValue"]',
        '//*[@class="some.value"]/i/div',
        '//*[@class="some_value"]/i/div',
        '//*[@class="some-value"]/i/div'
    )
)
def test_class_equals(value, child, expected_output):
    assert xpath.class_equals(value, child) == expected_output


@mark.parametrize(
    ('value', 'child', 'expected_output'),
    (
        ('someValue', '', '//*[contains(@name, "someValue")]'),
        ('some.value', '/i/div', '//*[contains(@name, "some.value")]/i/div'),
        ('some_value', '/i/div', '//*[contains(@name, "some_value")]/i/div'),
        ('some-value', '/i/div', '//*[contains(@name, "some-value")]/i/div'),
    ),
    ids=(
        '//*[contains(@name, "someValue")]',
        '//*[contains(@name, "some.value")]/i/div',
        '//*[contains(@name, "some_value")]/i/div',
        '//*[contains(@name, "some-value")]/i/div'
    )
)
def test_name_contains(value, child, expected_output):
    assert xpath.name_contains(value, child) == expected_output


@mark.parametrize(
    ('value', 'child', 'expected_output'),
    (
        ('someValue', '', '//*[@name="someValue"]'),
        ('some.value', '/i/div', '//*[@name="some.value"]/i/div'),
        ('some_value', '/i/div', '//*[@name="some_value"]/i/div'),
        ('some-value', '/i/div', '//*[@name="some-value"]/i/div'),
    ),
    ids=(
        '//*[@name="someValue"]',
        '//*[@name="some.value"]/i/div',
        '//*[@name="some_value"]/i/div',
        '//*[@name="some-value"]/i/div'
    )
)
def test_name_equals(value, child, expected_output):
    assert xpath.name_equals(value, child) == expected_output


@mark.parametrize(
    ('value', 'child', 'expected_output'),
    (
        ('someValue', '', '//*[contains(text(), "someValue")]'),
        ('some.value', '/i/div', '//*[contains(text(), "some.value")]/i/div'),
        ('some_value', '/i/div', '//*[contains(text(), "some_value")]/i/div'),
        ('some-value', '/i/div', '//*[contains(text(), "some-value")]/i/div'),
    ),
    ids=(
        '//*[contains(text(), "someValue")]',
        '//*[contains(text(), "some.value")]/i/div',
        '//*[contains(text(), "some_value")]/i/div',
        '//*[contains(text(), "some-value")]/i/div'
    )
)
def test_text_contains(value, child, expected_output):
    assert xpath.text_contains(value, child) == expected_output


@mark.parametrize(
    ('value', 'child', 'expected_output'),
    (
        ('someValue', '', '//*[text()="someValue"]'),
        ('some.value', '/i/div', '//*[text()="some.value"]/i/div'),
        ('some_value', '/i/div', '//*[text()="some_value"]/i/div'),
        ('some-value', '/i/div', '//*[text()="some-value"]/i/div'),
    ),
    ids=(
        '//*[text()="someValue"]',
        '//*[text()="some.value"]/i/div',
        '//*[text()="some_value"]/i/div',
        '//*[text()="some-value"]/i/div'
    )
)
def test_text_equals(value, child, expected_output):
    assert xpath.text_equals(value, child) == expected_output
