<h1>REDIS</h1>

<h3>Путь до конфига:</h3>

```shell
/etc/redis/redis.conf
```

<h2>Установка</h2>
```shell
sudo apt install redis-server
```
Прописываем в конфиге supervised no на supervised sytemd и перезапускаем сервис.

Строка для изменения:

```shell
supervised no
```

Перезапуск сервиса:

```shell
systemctl restart redis
```


<h2>Включение аунтефикации с паролем</h2>

Прописываем в конфиге пароль и перезапускаем сервис.

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


