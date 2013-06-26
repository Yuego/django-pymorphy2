#coding: utf-8
from __future__ import unicode_literals, absolute_import

import warnings
from django_pymorphy2.shortcuts import tokenizers

__all__ = ['process_phrase']


def process_phrase(phrase, func, forms, *args, **kwargs):
    """
    Обрабатывает фразу по словам с помощью переданной функции
    """
    words = tokenizers.extract_tokens(phrase)
    result = []
    try:
        for word in words:
            if tokenizers.GROUPING_SPACE_REGEX.match(word):
                result.append(word)
                continue
            result.append(func(word, forms, *args, **kwargs))
    except Exception as e:
        """
        Не уверен, как поступить правильно
        То ли бросать исключение, то ли просто возвращать исходную фразу
        Пока выбрал второй вариант
        """
        warnings.warn(e.message)
        return phrase

    return ''.join(result)
