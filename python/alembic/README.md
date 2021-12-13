<h1>Alembic</h1>
Инициализация:

```shell
alembic init alembic
```

`alembic.ini` - файл с конфигурацией (здесь прописываются параметры для подключения к базе данных)

`script.py.mako` - шаблон для новых миграций

`alembic/env.py` - кастомизация. Тут подключается объект MetaData SqlAlchemy. `target_metadata`


Генерация миграций:
```shell
alembic -c <path to alembic.ini> revision --message="Initial" --autogenerate
```

Накатить миграции:
```shell
alembic upgrade head
```

Откатить миграции:
```shell
alembic downgrade -1
```
