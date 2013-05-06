#coding: utf-8
from __future__ import unicode_literals, absolute_import

from .contstants import RU_CASES, RU_NUMBERS

__all__ = ['get_forms_set']


def get_forms_set(*args):
    forms = list()
    for arg in args:
        for key in arg.split(','):
            if key in RU_CASES:
                forms.append(RU_CASES[key])
            elif key in RU_NUMBERS:
                forms.append(RU_NUMBERS[key])
            else:
                raise ValueError('`%s` is not a grammeme' % key)
    return set(forms)