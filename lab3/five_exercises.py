#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def map_(func, iterable):
    """
    The same as built-in map(), but generator

    >>> from collections import Generator
    >>> square = lambda x: x ** 2
    >>> isinstance(map_(square, range(10)), Generator)
    True
    >>> list(map_(square, range(10)))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    for it in iter(iterable):
        it = func(it)
        yield it


def zip_(*iterables):
    """
    The same as built-in zip(), but generator

    >>> for i, j, k in zip_(range(3), range(4), range(-7, 0)):
    ...     print(i, j, k)
    0 0 -7
    1 1 -6
    2 2 -5

    """
# s: https://docs.python.org/3/library/functions.html
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


def dropwhile(predicate, iterable):
    """
    The same as itertools.dropwhile(), but generator

    >>> from collections import Generator
    >>> isinstance(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]), Generator)
    True
    >>> list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
    [6, 4, 1]
    """
# s: https://docs.python.org/3.1/library/itertools.html#itertools.dropwhile
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x


def filterfalse(predicate, iterable):
    """
    The same as itertools.filterfalse(), but generator

    >>> from collections import Generator
    >>> isinstance(filterfalse(lambda x: x % 2, range(10)), Generator)
    True
    >>> list(filterfalse(lambda x: x % 2, range(10)))
    [0, 2, 4, 6, 8]
    """
# s: https://docs.python.org/3.1/library/itertools.html#itertools.filterfalse
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x


def unique(iterable):
    """
    Generates unique values from iterable object

    >>> from collections import Generator
    >>> isinstance(unique(range(10)), Generator)
    True
    >>> list(unique([1, 1, 2, 2, 3, 1, 11, -1]))
    [1, 2, 3, 11, -1]
    """
    new = []
    for el in iterable:
        if el not in new:
            new.append(el)
            yield el


if __name__ == "__main__":
    import doctest
    doctest.testmod()
