================
djorm-hstore-editor
================

Поле модели с удобным виджетом для редактирования плоского массива HStore


Установка
==========

* Добавьте hstore_editor в INSTALLED_APPS
* Замените поле DictionaryField из состава djorm-ext-hstore на `hstore_editor.fields.DictionaryField`
* Выполните python manage.py collectstatic

Пример:
-------
.. image:: http://habrastorage.org/storage2/94c/2aa/60b/94c2aa60b99d1f6110d82a7b26d60bc5.png
