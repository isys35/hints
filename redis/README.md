<h1>REDIS</h1>

<h2>Включение аунтефикации с паролем</h2>

Прописываем в конфиге пароль и перезапускаем сервис.

Путь до конфига:

```shell
/etc/redis/redis.conf
```

Строка для изменения:

```shell
# requirepass вашпароль
```

Перезапуск сервиса:

```shell
systemctl restart redis
```

<h2>Комманды:</h2>
<b>SCAN</b> - выполняет итерацию набора ключей в текущей выбранной базе данных Redis.
```shell
scan <cursor> MATCH <match> COUNT <count>
```


<b>DEL</b> - удаляет данные по ключу.
```shell
del key
```


