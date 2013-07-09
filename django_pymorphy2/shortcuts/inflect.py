#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.template import TemplateSyntaxError

from pymorphy2.shapes import restore_word_case

from django_pymorphy2.config import morph
from django_pymorphy2.constants import DONT_INFLECT_FORMS
from .phrase import process_phrase

__all__ = ['inflect_word', 'inflect_phrase']


def inflect_word(word, forms, specifying_forms=None):
    """
    Склоняет одно слово в переданную форму
    """
    parsed = morph.parse(word)

    for p in parsed:
        if p.tag.POS in DONT_INFLECT_FORMS:
            return word
        else:
            # Нам необходима определенная словоформа. Остальные пропускаем

            if isinstance(specifying_forms, set) and specifying_forms not in p.tag:
                continue

            parsed_word = p.inflect(forms)
            if parsed_word is not None:
                return restore_word_case(parsed_word.word, word)

    return word


def inflect_word_from_nomn(word, forms, *args, **kwargs):
    parsed = morph.parse(word)

    forms_cache = []
    for p in parsed:
        if p.tag.POS in DONT_INFLECT_FORMS:
            return word
        else:
            # Нам необходима определенная словоформа. Остальные пропускаем
            if forms in p.tag:
                return p.word

            if 'nomn' not in p.tag:
                continue

            forms_cache.append(p)

    if len(forms_cache) > 0:
        p = forms_cache[0]
        parsed_word = p.inflect(forms)

        if parsed_word is not None:
            return restore_word_case(parsed_word.word, word)

    return word

def inflect_phrase(phrase, forms, *args, **kwargs):
    """
    Склоняет фразу в переданную форму пословно

    forms - кортеж, содержащий в себе 2 множества:
        первое - целевая форма,
        второе - уточнение, какую словоформу использовать

        tuple({'gent', 'plur'}, {'Name'})

        второй элемент кортежа указывать не обязательно

    """
    return process_phrase(phrase, inflect_word, forms, *args, **kwargs)

def inflect_collocation_phrase(phrase, forms, *args, **kwargs):
    return process_phrase(phrase, inflect_word_from_nomn, forms, *args, **kwargs)