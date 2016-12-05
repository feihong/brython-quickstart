"""
Unfortunately, trying to import asyncio results in an error.

"""
import asyncio

from util import bind


@bind('button.simple', 'click')
def simple(evt):
    print('Nothing to see yet')
