#coding: utf-8
from __future__ import unicode_literals, absolute_import

import json

from django.conf import settings
from django import forms
from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


class HstoreEditorWidget(forms.Widget):

    def __init__(self, *args, **kwargs):
        self._key = kwargs.pop('key_name', 'key')
        self._val = kwargs.pop('val_name', 'val')
        self.separator = kwargs.pop('separator', '__')
        self.key_label = kwargs.pop('key_label', _('Key'))
        self.value_label = kwargs.pop('value_label', _('Value'))
        self.add_label = kwargs.pop('add_label', _('add value'))
        self.del_label = kwargs.pop('del_label', _('delete value'))
        super(HstoreEditorWidget, self).__init__(*args, **kwargs)

    def _render_field(self, name, value, attrs=None):
        attrs = self.build_attrs(attrs, type='text', name=name, id='id_' + name)
        attrs['value'] = force_unicode(value) if value else ''
        return '<input{} />'.format(flatatt(attrs))

    def _render_item(self, name, idx, k, v):
        k_name = '{}__{}__{}'.format(name, self._key, idx)
        v_name = '{}__{}__{}'.format(name, self._val, idx)

        k_attrs = {
            'placeholder': self.key_label,
        }
        v_attrs = {
            'placeholder': self.value_label,
        }

        key_field = self._render_field(k_name, k, k_attrs)
        value_field = self._render_field(v_name, v, v_attrs)

        return ('<li>{}:{}'
                ' <a href="#" data-del-item="" title="{}">X</a></li>'
                ''.format(key_field, value_field, self.del_label))

    def _render_list(self, name, value, attrs):
        items = []
        idx = 0
        if value:
            for idx, (k, v) in enumerate(value.items()):
                items.append(self._render_item(name, idx, k, v))
        else:
            items.append(self._render_item(name, idx, '', ''))

        js = """<script type="text/javascript">
            (function($){
                var $list = $('#%(id)s');
                var item_template = '%(item_template)s';
                var counter = %(index)i;

                $('[data-add-item=%(id)s]').click(function(){
                    counter = counter + 1;
                    var new_item = item_template.replace(/IDX/g, counter);
                    var $new_item = $(new_item);
                    $list.append($new_item);
                });

                $list.on('click', 'a[data-del-item]', function(){
                    $(this).parent().remove();
                });
            })(jQuery || django.jQuery);
        </script>""" % {
            'id': attrs['id'],
            'item_template': self._render_item(name, 'IDX', '', ''),
            'index': idx,
        }

        html = ('<div class="hstore-editor">'
                '<ul%(attrs)s>%(items)s</ul>'
                '<a href="#" data-add-item="%(id)s">%(add_label)s</a></div>'
                '') % {'id': attrs['id'],
                       'attrs': flatatt(attrs),
                       'items': ''.join(items),
                       'add_label': self.add_label,
                       }

        return "\n".join([html, js])

    def value_from_datadict(self, data, files, name):

        json_data = {}
        for k, v in data.iteritems():
            if k.startswith(name) and self.separator in k:
                typ, idx = k.rsplit(self.separator)[-2:]
                json_data.setdefault(idx, {})[typ] = v if v else None

        data_dict = dict((x[self._key], x[self._val]) for x in json_data.values() if x[self._key])
        return json.dumps(data_dict)

    def render(self, name, value, attrs=None):
        value = json.loads(value)
        return mark_safe(self._render_list(name, value, attrs))

    class Media:
        css = {
            'screen': [
                '{}hstore_editor/hstore_editor.css'.format(settings.STATIC_URL)
            ]
        }