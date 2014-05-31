#!/usr/bin/env python
from distutils.core import setup
import sys
sys.path.insert(0, '..')

from django_pymorphy2.version import __version__

for cmd in ('egg_info', 'develop', 'build_sphinx', 'upload_sphinx'):
    if cmd in sys.argv:
        from setuptools import setup

setup(
    name='django_pymorphy2',
    version=__version__,
    author= 'Artem Vlasov',
    author_email='root@proscript.ru',
    url='https://github.com/Yuego/django-pymorphy2',
    download_url='https://github.com/Yuego/django-pymorphy2/archive/%s.tar.gz' % __version__,

    description='Django and PyMorphy2 integration',
    long_description=open('README.rst').read() + open('AUTHORS.rst').read(),

    license='MIT license',
    requires=[
        'django (>=1.3)',
        'pymorphy2 (>=0.7)',
        'pymorphy2_dicts',
        'six',
    ],
    packages=[
        'django_pymorphy2',
        'django_pymorphy2.shortcuts',
        'django_pymorphy2.templatetags',
    ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
