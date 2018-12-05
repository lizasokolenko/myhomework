#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date


class Person:
    """
    >>> p = Person('Ivan', 'Ivanov', 'male', date(1989, 4, 26))
    >>> print(p)
    Ivan Ivanov, male, 29 years

    >>> p.full_ages()
    29
    >>> Person('Ivan', 'Ivanov', 'man', "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: bday must be date type
    """

    def __init__(self, name, surname, sex, bday):
        self.name = name
        self.surname = surname
        self.sex = sex
        if type(bday) == date:
            self.month = bday.month
            self.year = bday.year
            self.day = bday.day
            self.bday = bday
        else:
            raise ValueError('bday must be date type')

    def __str__(self):
        return '{} {}, {}, {} years'.format(self.name, self.surname, self.sex, self.full_ages())

    def full_ages(self):
        today = date.today()
        bday = self.bday
        full_age = today.year - bday.year
        if today.month < bday.month:
            full_age -= 1
        elif today.month == bday.month and today.day < bday.day:
            full_age -= 1
        return full_age
        # raise NotImplementedError


class Student(Person):
    """
    >>> s = Student('Ivan', 'Ivanov', 'male', date(1989, 4, 26), 161, 9)
    >>> print(s)
    Ivan Ivanov, male, 29 years, 161 group, 9 skill
    """
    def __init__(self, name, surname, sex, bday, group, skill):
        super(Student, self).__init__(name=name, surname=surname, sex=sex, bday=bday)
        self.group = group
        self.skill = skill

    def __str__(self):
        return '{} {}, {}, {} years, {} group, {} skill'.format(self.name, self.surname,
                                                                self.sex, self.full_ages(), self.group, self.skill)
        # raise NotImplementedError


class Group:
    """Encapsulates list of students"""

    def __init__(self, group):
        self._group = group

    def __str__(self):
        str = ["Student({})".format(s) for s in self._group]
        return "Group({})".format(str)

    def sort_by_age(self, reverse=False):
        n = 1
        while n < len(self._group):
            for i in range(len(self._group) - n):
                if self._group[i].full_ages() > self._group[i + 1].full_ages():
                    self._group[i], self._group[i + 1] = self._group[i + 1], self._group[i]
            n += 1
        if reverse:
            self._group = self._group[::1]
        return self._group

    def sort_by_skill(self, reverse=False):
        n = 1
        while n < len(self._group):
            for i in range(len(self._group) - n):
                if self._group[i].skill > self._group[i + 1].skill:
                    self._group[i], self._group[i + 1] = self._group[i + 1], self._group[i]
            n += 1
        if reverse:
            self._group = self._group[::1]
        return self._group

    def sort_by_age_and_skill(self, reverse=False):
        self._group = self.sort_by_age(self._group)
        n = 1
        while n < len(self._group):
            for i in range(len(self._group) - n):
                if self._group[i].full_ages() == self._group[i + 1].full_ages():
                    if self._group[i].skill < self._group[i + 1].skill:
                        self._group[i], self._group[i + 1] = self._group[i + 1], self._group[i]
            n += 1
        if reverse:
            self._group = self._group[::1]
        return self._group
        # raise NotImplementedError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
