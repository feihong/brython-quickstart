from browser import window, timer
from javascript import JSConstructor


Promise = JSConstructor(window.Promise)
P = window.Promise

def get_chaining(url):
    """
    Unfortunately, this version does not work sends a Promise object to the
    next Promise in the chain.

    """
    def promise(resolve, reject):
        def got_response(response):
            print(response.status)
            return response.json()
        def got_obj(obj):
            resolve(obj)
        window.fetch(url).then(got_response).then(got_obj)
    return Promise(promise)


def get(url):
    def callback(resolve, reject):
        def got_response(response):
            print(response.status)
            response.json().then(got_obj)
        def got_obj(obj):
            resolve(obj)
        window.fetch(url).then(got_response)
    return Promise(callback)


def sleep(secs):
    def callback(resolve, reject):
        timer.set_timeout(resolve, secs * 1000)
    return Promise(callback)
