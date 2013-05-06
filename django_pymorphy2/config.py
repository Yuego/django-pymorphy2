#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf import settings

from .morph import morph

__all__ = ['morph', 'MARKER_OPEN', 'MARKER_CLOSE']


MARKER_OPEN = getattr(settings, 'PYMORPHY_MARKER_OPEN', '\[\[')
MARKER_CLOSE = getattr(settings, 'PYMORPHY_MARKER_CLOSE', '\]\]')