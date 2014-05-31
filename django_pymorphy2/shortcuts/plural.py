#coding: utf-8
from __future__ import unicode_literals, absolute_import

import six

from pymorphy2.shapes import restore_capitalization

from django_pymorphy2.config import morph
from .phrase import process_phrase

__all__ = ['pluralize_word', 'pluralize_phrase']


def pluralize_word(word, number):
    """
    Согласует слово с числом
    """
    assert isinstance(number, six.integer_types)

    parsed = morph.parse(word)
    if isinstance(parsed, list):
        pluralized = parsed[0].make_agree_with_number(number)
        if pluralized is not None:
            return restore_capitalization(pluralized.word, word)

    return word


def pluralize_phrase(phrase, number):
    """
    Согласует фразу с числом пословно
    """
    return process_phrase(phrase, pluralize_word, *(number,))
