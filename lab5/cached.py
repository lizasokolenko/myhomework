#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def cached(func):
    """
    >>> @cached
    ... def add(a, b):
    ...     print(a, b)
    ...     return a + b
    ...
    >>> add(1, 2)
    1 2
    3
    >>> add(1, 2)
    3
    >>> add(2, 2)
    2 2
    4
    >>> add(2, 2)
    4
    """
    result = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_kwargs = tuple(kwargs.items())
        new_list = (args, new_kwargs)
        if new_list not in result:
                results = func(*args, **kwargs)
                result[new_list] = results
        return result[new_list]

    return wrapper


if __name__ == '__main__':
    import doctest
    doctest.testmod()
