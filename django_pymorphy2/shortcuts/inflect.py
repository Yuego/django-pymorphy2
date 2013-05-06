#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django_pymorphy2.config import morph
from django_pymorphy2.contrib import get_forms_set, tokenizers, DONT_INFLECT, restore_word_case


def inflect_word(word, forms):
    parsed = list(morph.parse(word))

    for p in parsed:
        if p.tag.POS in DONT_INFLECT:
            return word
        else:
            parsed_word = parsed[0].inflect(get_forms_set(forms))
            if parsed_word is not None:
                return restore_word_case(parsed_word.word, word)

    return word


def inflect_phrase(phrase, forms):
    words = tokenizers.extract_tokens(phrase)
    result = ""
    try:
        for word in words:
            if tokenizers.GROUPING_SPACE_REGEX.match(word):
                result += word
                continue
            result += inflect_word(word, forms)
    except ValueError as e:
        raise
    except Exception as e:
        raise

    return result