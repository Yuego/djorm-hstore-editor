#coding: utf-8
from __future__ import unicode_literals, absolute_import

from djorm_hstore.fields import DictionaryField as DF
from .widgets import HstoreEditorWidget

class DictionaryField(DF):

    def formfield(self, **params):
        defaults = {
            'widget': HstoreEditorWidget
        }
        defaults.update(params)
        return super(DictionaryField, self).formfield(**defaults)