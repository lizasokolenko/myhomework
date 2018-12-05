#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt


class Vector:
    """
    Class Vector is n-dimensional geometry vector.

    Examples of usage:

    >>> a = Vector([1, 2, 3, 4])
    >>> b = Vector([0, 1, -1, -4])
    >>> a
    Vector([1, 2, 3, 4])
    >>> a + b
    Vector([1, 3, 2, 0])
    >>> a - b
    Vector([1, 1, 4, 8])
    >>> print(a * b)
    Vector([0, 2, -3, -16])
    >>> print(b / a)
    Vector([0.0, 0.5, -0.3333333333333333, -1.0])
    >>> a == Vector([1, 2, 3, 4])
    True
    >>> a.append(144)
    >>> print(a)
    Vector([1, 2, 3, 4, 144])
    >>> len(a)
    5
    >>> a.ndim() == 5
    True
    >>> a[1] == 2
    True
    >>> a[-1] = 5
    >>> a[-1]
    5
    >>> a.clear()
    >>> not a
    True
    >>> b.reverse()
    >>> b
    Vector([-4, -1, 1, 0])
    >>> abs(b) == sqrt(16 + 1 + 1 + 0)
    True
    >>> b.argmin()
    0
    >>> b[b.argmin()] == -4
    True
    >>> b.argmax()
    2
    >>> b[b.argmax()] == 1
    True
    >>> [i for i in b] == [-4, -1, 1, 0]
    True
    """
    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return 'Vector({})'.format(self.vector)

    def __repr__(self):
        return '{}'.format(self)

    def __add__(self, other):
        sum = []
        for n in range(len(self.vector)):
            sum.append(self.vector[n] + other.vector[n])
        return Vector(sum)

    def __sub__(self, other):
        sub = []
        for n in range(len(self.vector)):
            sub.append(self.vector[n] - other.vector[n])
        return Vector(sub)

    def __mul__(self, other):
        mul = []
        for n in range(len(self.vector)):
            mul.append(self.vector[n] * other.vector[n])
        return 'Vector({})'.format(mul)

    def __truediv__(self, other):
        div = []
        for n in range(len(self.vector)):
            if other.vector[n] == 0:
                div.append(0.0)
            else:
                div.append(self.vector[n]/other.vector[n])
        return 'Vector({})'.format(div)

    def __len__(self):
        return len(self.vector)

    def append(self, elem):
        self.vector.append(elem)

    def __abs__(self):
        abs = 0
        for el in self.vector:
            abs += el ** 2
        abs = sqrt(abs)
        return abs

    def ndim(self):
        return len(self.vector)

    def clear(self):
        return self.vector.clear()

    def __getitem__(self, item):
        return self.vector[item]

    def __setitem__(self, key, value):
        self.vector[key] = value

    def reverse(self):
        self.vector = self.vector[::-1]

    def argmax(self):
        max_el = self.vector[0]
        x = 0
        for n in range(len(self.vector)):
            if self.vector[n] > max_el:
                x = n
                max_el = self.vector[n]
        return x

    def argmin(self):
        min_el = self.vector[0]
        x = 0
        for n in range(len(self.vector)):
            if self.vector[n] < min_el:
                x = n
                min_el = self.vector[n]
        return x

    def __eq__(self, other):
        tr = self.vector == other
        return tr
    # raise NotImplementedError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
