from browser import document


def bind(selector, event_name):
    """
    Decorator to make it easier to define event callbacks.

    """
    def inner(fn):
        for el in document.get(selector=selector):
            el.bind(event_name, fn)
    return inner
