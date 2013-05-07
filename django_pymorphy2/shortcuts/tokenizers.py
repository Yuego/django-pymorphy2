# -*- coding: utf-8 -*-
"""
    Взято из https://github.com/kmike/pymorphy
"""
import re

__all__ = ['GROUPING_SPACE_REGEX',
           'extract_tokens']

GROUPING_SPACE_REGEX = re.compile('([^\w_-]|[+])', re.U)


def extract_tokens(text):
    """
    Разбивает текст на токены - слова, пробелы, знаки препинания и возвращает
    полученный массив строк.
    """
    return filter(None, GROUPING_SPACE_REGEX.split(text))
