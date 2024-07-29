
def attribute_contains(element: str, attribute: str, value: str, child: str = '') -> str:
    return f'//{element}[contains({attribute}, "{value}")]{child}'

def attribute_equals(element: str, attribute: str, value: str, child: str = '') -> str:
    return f'//{element}[{attribute}, "{value}"]{child}'

def id_contains(value: str, child: str = '') -> str:
    return attribute_contains('*', '@id', value, child)

def id_equals(value: str, child: str = '') -> str:
    return attribute_equals('*', '@id', value, child)

def class_contains(value: str, child: str = '') -> str:
    return attribute_contains('*', '@class', value, child)

def class_equals(value: str, child: str = '') -> str:
    return attribute_equals('*', '@class', value, child)

def name_contains(value: str, child: str = '') -> str:
    return attribute_contains('*', '@name', value, child)

def name_equals(value: str, child: str = '') -> str:
    return attribute_equals('*', '@name', value, child)

def text_contains(value: str, child: str = '') -> str:
    return attribute_contains('*', 'text()', value, child)

def text_equals(value: str, child: str = '') -> str:
    return attribute_equals('*', 'text()', value, child)
