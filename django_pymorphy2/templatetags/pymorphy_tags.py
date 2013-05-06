#coding: utf-8
from __future__ import unicode_literals, absolute_import

"""
    Создано на основе
    https://github.com/kmike/pymorphy/blob/master/pymorphy/templatetags/pymorphy_tags.py

"""
import re

from django import template
from django.utils.text import force_unicode

from django_pymorphy2.config import morph, MARKER_OPEN, MARKER_CLOSE
from django_pymorphy2.contrib import tokenizers, get_forms_set

register = template.Library()

markup_re = re.compile('(%s.+?%s)' % (MARKER_OPEN, MARKER_CLOSE), re.U)


def _process_phrase(phrase, forms, *args, **kwargs):
    words = tokenizers.extract_tokens(phrase)
    result = ""
    try:
        for word in words:
            if tokenizers.GROUPING_SPACE_REGEX.match(word):
                result += word
                continue
            parsed = morph.parse(word)[0]
            result += parsed.inflect(get_forms_set(forms)).word
    except ValueError as e:
        raise template.TemplateSyntaxError(e)
    except Exception as e:
        raise template.TemplateSyntaxError([e.message, word, forms, parsed.inflect(get_forms_set(forms))])

    return result


def _process_marked_phrase(phrase, forms, *args, **kwargs):
    """
    Обработать фразу. В фразе обрабатываются только куски, заключенные
    в двойные квадратные скобки (например, "[[лошадь]] Пржевальского").
    """
    def process(m):
        return _process_phrase(m.group(1)[2:-2], forms)

    return re.sub(markup_re, process, phrase)


def _process_unmarked_phrase(phrase, forms, *args, **kwargs):
    """
    Обработать фразу. В фразе не обрабатываются куски, заключенные
    в двойные квадратные скобки (например, "лошадь [[Пржевальского]]").
    """
    def process(part):
        if not re.match(markup_re, part):
            return _process_phrase(part, forms)
        return part[2: -2]

    parts = [process(s) for s in re.split(markup_re, phrase)]
    return ''.join(parts)


@register.filter
def inflect(phrase, forms):
    if not phrase:
        return phrase
    return _process_unmarked_phrase(force_unicode(phrase), force_unicode(forms))


@register.filter
def inflect_marked(phrase, forms):
    if not phrase:
        return phrase
    return _process_marked_phrase(force_unicode(phrase), force_unicode(forms))

