from __future__ import print_function

import re
from builtins import str


class Converter(object):
    def __init__(self, split, valid, action):
        self.pattern = re.compile(split, re.UNICODE)
        self.word_cls = get_word_cls(valid, action)

    def __call__(self, text):
        words = []

        word = None
        for string in self.pattern.split(text):
            word = self.word_cls(string, prev=word)
            words.append(word)

        return ''.join(map(str, words))


def applier(*funcs):
    def _(word):
        for func in funcs:
            word = func(word)
        return word

    return _


def get_word_cls(valid, action):
    valid = set(valid)

    class Word(object):
        def __init__(self, word='', prev=None, next_=None):
            self._word = word
            self._prev = prev
            self._next = next_
            if prev is not None:
                prev.set_next(self)

        def __repr__(self):
            return repr(self._word)

        def __str__(self):
            if not self:
                return self._word

            orig = self._word
            p, n = self.get_prev(), self.get_next()
            action(self)

            if orig.isupper() and (p and p.is_upper() or n and n.is_upper()):
                return self._word.upper()

            if self._word and orig.istitle():
                return self._word[0].upper() + self._word[1:].lower()

            return self._word

        def __bool__(self):
            return not set(self._word.upper()) - valid

        def has_stop(self):
            if self._next is not None:
                return self._next.get_word() not in " -\u2010"

        def get_next(self):
            if self._next is not None:
                return self._next if self._next else self._next.get_next()

        def get_prev(self):
            if self._prev is not None:
                return self._prev if self._prev else self._prev.get_prev()

        def get_word(self):
            return self._word

        def is_upper(self):
            return self._word.isupper()

        def set_next(self, next_):
            self._next = next_

        def __add__(self, other):
            self._word += other
            return self

        def __radd__(self, other):
            self._word = other + self._word
            return self

        def apply(self, func, index=0):
            self._word = self._word[:index] + func(self._word[index:])
            return self

        def replace(self, old, new):
            self._word = self._word.replace(old, new)
            return self

        def re_replace(self, pattern, new):
            self._word = new.join(t for t in pattern.split(self._word))
            return self

        def startswith(self, prefix):
            return self._word.startswith(prefix)

        def strip(self, chars):
            self._word = self._word.strip(chars)
            return self

        def lstrip(self, chars):
            self._word = self._word.lstrip(chars)
            return self

        def translate(self, table):
            self._word = self._word.translate(table)
            return self

        def upper(self):
            self._word = self._word.upper()
            return self

    return Word


def replacer(table):
    def _(word):
        for i, o in table.items():
            word = word.replace(i, o)
        return word

    return _


def translator(*args):
    trans = str.maketrans(*args)

    def _(word):
        return word.translate(trans)

    return _
