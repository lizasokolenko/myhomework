#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A:
    _init = 0

    def __init__(self, **kwargs):
        A._init += 1
        for key, value in kwargs.items():
            setattr(self, key, value)


class B(A):
    _init = 0

    def __init__(self, *args, **kwargs):
        B._init += 1
        if len(args) > 0:
            arg_dict = dict(a=args[2], b1=args[0], b2=args[1])
        else:
            arg_dict = {}
        super().__init__(**arg_dict, **kwargs)


class C(A):
    _init = 0

    def __init__(self, *args, **kwargs):
        C._init += 1
        if len(args) > 0:
            arg_dict = dict(a=args[2], c1=args[0], c2=args[1])
        else:
            arg_dict = {}
        super().__init__(**arg_dict, **kwargs)


class D(B, C):
    _init = 0

    def __init__(self, d1, d2, b1, b2, c1, c2, a, **kwargs):
        D._init += 1
        arg_dict = {'d1': d1, 'd2': d2, 'b1': b1, 'b2': b2,
                    'c1': c1, 'c2': c2, 'a': a}
        super().__init__(**arg_dict, **kwargs)


def main():
    pass


if __name__ == "__main__":
    main()
