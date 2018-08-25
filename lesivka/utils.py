from __future__ import print_function

import re
from builtins import str


def applier(*funcs):
    def apply(text):
        for func in funcs:
            text = func(text)
        return text

    return apply


def replacer(d):
    def replace(text):
        for i, o in d.items():
            text = text.replace(i, o)
        return text

    return replace


def splitter(pattern, action):
    re_pat = re.compile(pattern, flags=re.UNICODE)

    def split(text):
        result = (action.apply(word) for word in re_pat.split(text))
        return ''.join(result)

    return split


def translator(*args):
    trans = str.maketrans(*args)

    def translate(text):
        return text.translate(trans)

    return translate
