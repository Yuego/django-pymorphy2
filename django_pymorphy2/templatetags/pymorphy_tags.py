#coding: utf-8
from __future__ import unicode_literals, absolute_import

"""
    Создано на основе
    https://github.com/kmike/pymorphy/blob/master/pymorphy/templatetags/pymorphy_tags.py

"""
import re

from django import template
from django.utils.text import force_text

from django_pymorphy2.config import MARKER_OPEN, MARKER_CLOSE
from django_pymorphy2.shortcuts.forms import get_forms_tuple
from django_pymorphy2.shortcuts.inflect import inflect_phrase, inflect_collocation_phrase
from django_pymorphy2.shortcuts.plural import pluralize_phrase

register = template.Library()

markup_re = re.compile('(%s.+?%s)' % (MARKER_OPEN, MARKER_CLOSE), re.U)


def _process_marked_phrase(phrase, func, *args, **kwargs):
    """
    Обработать фразу. В фразе обрабатываются только куски, заключенные
    в двойные квадратные скобки (например, "[[лошадь]] Пржевальского").
    """
    def process(m):
        return func(m.group(1)[2:-2], *args, **kwargs)

    return re.sub(markup_re, process, phrase)


def _process_unmarked_phrase(phrase, func, *args, **kwargs):
    """
    Обработать фразу. В фразе не обрабатываются куски, заключенные
    в двойные квадратные скобки (например, "лошадь [[Пржевальского]]").
    """
    def process(part):
        if not re.match(markup_re, part):
            return func(part, *args, **kwargs)
        return part[2: -2]

    parts = [process(s) for s in re.split(markup_re, phrase)]
    return ''.join(parts)


@register.filter
def inflect(phrase, forms):
    if not phrase or not forms:
        return phrase
    return _process_unmarked_phrase(force_text(phrase), inflect_phrase, *get_forms_tuple(forms))


@register.filter
def inflect_marked(phrase, forms):
    if not phrase or not forms:
        return phrase
    return _process_marked_phrase(force_text(phrase), inflect_phrase, *get_forms_tuple(forms))


@register.filter
def inflect_collocation(phrase, forms):
    if not phrase or not forms:
        return phrase
    return _process_unmarked_phrase(force_text(phrase), inflect_collocation_phrase, *get_forms_tuple(forms))


@register.filter
def plural(phrase, number):
    if not phrase or not number:
        return phrase
    return _process_unmarked_phrase(force_text(phrase), pluralize_phrase, number)
