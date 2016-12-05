import random
from functools import partial

from browser import document, window
from browser import timer

import greeting
from promise import Promise, P, sleep, get


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
    document['content'].text = greeting.get_greeting()


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


@bind('button.timeout', 'click')
def timeout(evt):
    """
    Using timer.set_timeout() gives you a nicer-looking console message when an
    exception is raised.

    """

    # timer.set_timeout(partial(print, 'Using set_timeout'), 100)
    # window.setTimeout(partial(print, 'Using setTimeout'), 200)

    def bad_callback():
        z = 7/0

    timer.set_timeout(bad_callback, 300)
    # window.setTimeout(bad_callback, 400)


@bind('button.generator', 'click')
def generator(evt):
    def count(n):
        for i in range(1, n+1):
            yield i
        return chr(random.randint(65, 80))

    gen = count(7)
    while True:
        try:
            print('Number:', next(gen))
        except StopIteration as stop:
            print('Generator return value:', stop.value)
            break


@bind('button.sleep', 'click')
def promise_1(evt):
    print('Sleeping for 3 seconds...')
    def done_sleeping(val):
        print('Woke up!')
    sleep(3).then(done_sleeping)


@bind('button.ajax', 'click')
def promise_2(evt):
    print('Fetching message.json...')
    def got_obj(obj):
        print('Response object:', obj)
        print('Response object (converted to dict):', obj.to_dict())
    get('message.json').then(got_obj)


@bind('button.chaining', 'click')
def promise_3(evt):
    """
    Unfortunately, chaining in Brython does not work as expected. The
    equivalent JavaScript is:

    Promise.resolve(5).then(x => Promise.resolve(x * 2)).then(x => console.log(x))

    When run in the browser, the output is 10. The output of this function is,
    for some reason, a Promise object.

    """
    def callback(val):
        print('Chaining result:', val.to_dict())
    P.resolve(5).then(lambda x: P.resolve(x * 2)).then(callback)
