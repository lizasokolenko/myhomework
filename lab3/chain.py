#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from collections import Iterable


def chain(*iterables):
    """
    >>> list(chain([[["test"]]]))
    ['t', 'e', 's', 't']
    """
    for iterable in iterables:
        if not isinstance(iterable, Iterable):
            yield iterable
        else:
            for item in iterable:
                if item != iterable:
                    yield from chain(item)
                else:
                    yield item


if __name__ == "__main__":
    import doctest
    doctest.testmod()
