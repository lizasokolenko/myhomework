#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps


def singleton(cls):
    """
    >>> @singleton
    ... class A:
    ...     pass

    >>> id(A()) == id(A()) == id(A())
    True
    """
    instances = {}

# https://pypi.org/project/singleton-decorator/
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper
    # raise NotImplementedError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
