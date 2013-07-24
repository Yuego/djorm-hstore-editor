================
djorm-hstore-editor
================

Поле модели с удобным виджетом для редактирования плоского массива HStore


Установка
==========

* Добавьте hstore_editor в INSTALLED_APPS
* Замените поле DictionaryField из состава djorm-ext-hstore на `hstore_editor.fields.DictionaryField`
* Выполните python manage.py collectstatic