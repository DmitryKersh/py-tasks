# Ежедневник

Ежедневник с консольным интерфейсом.

Реализуйте считывание команд, обработку ошибочного ввода (в том числе и некорректные аргументы команд) и вывод справки по командам (на `help`)

Для удобного вывода данных в виде таблиц можно использовать модуль `PrettyTable`

## Следующие команды должны поддерживаться:

* **`add_task`/`a`** - начинает диалог добавления задания. Спрашивает название, описание, дедлайн. Добавляет задание, помечая его уникальным id
* **`show_all`/`sa`** - выводит все задания: id, название, описание, дедлайн
* `show_on_fire` - спрашивает срок до конца и выводит задания с дедлайном менее срока. Поддерживать сроки типа: 5h, 2d... Составные типа 1y3d5h - по желанию
* **`resolve_task`/`r`** - помечает задание сделанным, спросив id
* `delete_task`/`d` - удаляет задание, спросив id
* `delete_resolved`/`dr` - удаляет сделанные задания
* `show_unresolved` - показывает несделанные задания
* `show_for_today` - показывает задания с дедлайном на сегодня
* `edit_task` - спрашивает id задания, затем обновляет его параметры
* `search_task` - спрашивает кусок названия, выводит все задания с похожим названием
* `show_expired` - показывает просроченные задания
* `delete_expired` - удаляет просроченные задания
* **`save`/`s`** - сохраняет всю информацию в файл
* **`exit`/`q`** - выход с вопросом: сохранить ли?
