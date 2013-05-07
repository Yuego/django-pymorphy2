#coding: utf-8
from __future__ import unicode_literals, absolute_import

"""
Граммема 	Значение 	Примеры
NOUN 	имя существительное 	        хомяк
ADJF 	имя прилагательное (полное) 	хороший
ADJS 	имя прилагательное (краткое) 	хорош
COMP 	компаратив 	                    лучше, получше, выше
VERB 	глагол (личная форма) 	        говорю, говорит, говорил
INFN 	глагол (инфинитив)              говорить, сказать
PRTF 	причастие (полное) 	            прочитавший, прочитанная
PRTS 	причастие (краткое) 	        прочитана
GRND 	деепричастие 	                прочитав, рассказывая
NUMR 	числительное 	                три, пятьдесят
ADVB 	наречие 	                    круто
NPRO 	местоимение-существительное 	он
PRED 	предикатив 	                    некогда
PREP 	предлог 	                    в
CONJ 	союз 	                        и
PRCL 	частица 	                    бы, же, лишь
INTJ 	междометие 	                    ой
"""

RU_NUMBERS = {
    'ед': 'sing',
    'мн': 'plur',
}

RU_CASES = {
    'им': 'nomn',
    'рд': 'gent',
    'дт': 'datv',
    'вн': 'accs',
    'тв': 'ablt',
    'пр': 'loct',
    'зв': 'voct',

    'рд1': 'gen1',
    'рд2': 'gen2',
    'вн2': 'acc2',
    'пр1': 'loc1',
    'пр2': 'loc2',
}

RU_GENDERS = {
    'мр': 'masc',
    'жр': 'femn',
    'ср': 'neut',
}
INFLECT_FORMS = dict()
map(INFLECT_FORMS.update, (RU_NUMBERS, RU_CASES, RU_GENDERS))

DONT_INFLECT_FORMS = ('COMP', 'ADVB', 'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ')

RU_FIO = {
    'имя': 'Name',
    'фам': 'Surn',
    'отч': 'Patr',
}

SPECIFYING_FORMS = dict()
map(SPECIFYING_FORMS.update, (RU_FIO,))