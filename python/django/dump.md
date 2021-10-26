<h3>Дамп базы данных</h3>

Дамп всей базы данных:

```shell script
python manage.py dumpdata > db.json
```

Дамп определённого приложения:

```shell script
python manage.py dumpdata admin > admin.json
```

Дамп определённой таблицы:

```shell script
python manage.py dumpdata admin.logentry > admin_logentry.json
```


Можно указать отступы с помощью ключа `--indent`

Можно искючить таблицы с помощью ключа `--exclude`

Импорт базы данных:

```shell script
python manage.py loaddata db.json
```
