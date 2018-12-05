#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def minimum(*args, **kwargs):
    """
    The same as built-in min (exclude default parameter).
    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.

    >>> minimum(1, 2, 3) == min(1, 2, 3)
    True
    >>> minimum([1, 2, 3]) == min([1, 2, 3])
    True
    """
    if len(args) > 1:
        it = iter(args)
    else:
        it = iter(args[0])
    min_el = next(it)
    for n in it:
        if n < min_el:
            min_el = n
    if 'key' in kwargs:
        for el in args:
            for i in iter(el):
                if kwargs['key'](i) < kwargs['key'](min_el):
                    min_el = i
    return min_el


def maximum(*args, **kwargs):
    """
    The same as built-in max (exclude default parameter).
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.

    >>> maximum(1, 2, 3) == max(1, 2, 3)
    True
    >>> maximum([1, 2, 3]) == max([1, 2, 3])
    True
    """
    if len(args) > 1:
        it = iter(args)
    else:
        it = iter(args[0])
    max_el = next(it)
    for n in it:
        if n > max_el:
            max_el = n
    if 'key' in kwargs:
        for el in args:
            for i in iter(el):
                if kwargs['key'](i) > kwargs['key'](max_el):
                    max_el = i
    return max_el


if __name__ == "__main__":
    import doctest
    doctest.testmod()
