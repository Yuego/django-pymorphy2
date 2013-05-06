#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from django.conf import settings
from django.core.management import call_command

sys.path.insert(0, '.')

settings.configure(
    INSTALLED_APPS=('django_pymorphy2',),
    DATABASES = {'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }}
)

if __name__ == "__main__":
    call_command('test', 'django_pymorphy2')
