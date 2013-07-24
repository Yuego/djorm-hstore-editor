#coding: utf-8
from __future__ import unicode_literals, absolute_import

from djorm_hstore.fields import DictionaryField as DF
from .widgets import HstoreEditorWidget

class DictionaryField(DF):

    def __init__(self, *args, **kwargs):
        self._widget_attrs = {}
        _widget_attrs = {
            'key_name': kwargs.pop('key_name', None),
            'val_name': kwargs.pop('val_name', None),
            'separator': kwargs.pop('separator', None),
            'key_label': kwargs.pop('key_label', None),
            'value_label': kwargs.pop('value_label', None),
            'add_label': kwargs.pop('add_label', None),
            'del_label': kwargs.pop('del_label', None),
        }
        for k, v in _widget_attrs.items():
            if v is not None:
                self._widget_attrs[k] = v

        super(DictionaryField, self).__init__(*args, **kwargs)

    def formfield(self, **params):
        defaults = {
            'widget': HstoreEditorWidget(**self._widget_attrs)
        }
        defaults.update(params)
        return super(DictionaryField, self).formfield(**defaults)

    def south_field_triple(self):
        from south.modelsinspector import introspector
        args, kwargs = introspector(self)
        return ('djorm_hstore.fields.DictionaryField', args, kwargs)