import random
from browser import document


GREETINGS = [
    'Hello World',
    'Hola Mundo',
    'ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ',
    'こんにちは世界',
    '你好世界',
    'Përshendetje Botë',
    'مرحبا بالعالم',
    'Բարեւ, աշխարհ',
    'হ্যালো দুনিয়া',
    'Saluton mondo',
    'გამარჯობა მსოფლიო',
]


def bind(selector, event_name):
    """
    Decorator to make it easier to define event callbacks.

    """
    def inner(fn):
        for el in document.get(selector=selector):
            el.bind(event_name, fn)
    return inner


@bind('button.change', 'click')
def change(evt):
    document['content'].text = random.choice(GREETINGS)


@bind('button.error', 'click')
def zero_division(evt):
    choice = random.randint(1, 3)
    if choice == 1:
        a = 1/0     # this would not trigger an exception in JS
    elif choice == 2:
        a = b + 1
    else:
        print(a.foobar)


@bind('button.debug', 'click')
def debug(evt):
    """
    The __debugger__ statement activates the JavaScript debugger. In the
    console, evaluate $locals.i to get the current value of i. Also,
    $locals.$line_info contains the line number and file.

    """
    nums = range(1, 10)
    for i in nums:
        c = chr(i + 64)
        if i == 5:
            __debugger__
        print('{} {}'.format(i, c))
