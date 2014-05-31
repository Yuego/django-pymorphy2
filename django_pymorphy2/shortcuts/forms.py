#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.utils.text import force_text
from django_pymorphy2.constants import INFLECT_FORMS, SPECIFYING_FORMS

__all__ = ['get_forms_tuple']


def get_forms_tuple(*args):
    """
    Преобразует строку граммем в кордеж с двумя множествами
     - множество тегов для склонения
     - множество тегов для уточнения словоформы
    """
    forms = list()
    specs = list()
    for arg in args:
        for key in force_text(arg).split(','):
            if key in INFLECT_FORMS:
                forms.append(INFLECT_FORMS[key])
            elif key in SPECIFYING_FORMS:
                specs.append(SPECIFYING_FORMS[key])
            else:
                raise ValueError('`%s` is not a grammeme' % key)

    return set(forms), set(specs)
