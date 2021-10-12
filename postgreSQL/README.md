<h1>PostgreSQL</h1>

<h3>Установка и настройка</h3>

1. Установка

```shell
sudo apt install postgresql postgresql-contrib
```

2. Вход в интерактивный режим пользователем postgres

```shell
sudo -u postgres psql
```

3. Создание пользователя

```sql
    CREATE USER <имя роли> WITH PASSWORD '<пароль>';
```

4. Создание базы данных

```sql
    CREATE DATABASE <имя бд>;
```

5. Добавляем права


```sql
    GRANT ALL PRIVILEGES ON DATABASE <имя бд> to <имя роли>;
```

Выход из интерактивного режима `\q`

6. Проверка 

```shell
psql -h localhost <имя бд> <имя роли>;
```


<h3>Настройка удалённого подключения к PostgreSQL</h3>

В файле конфигурации `postgresql.conf` находим и редактируем следующее:

```.editorconfig
listen_addresses = '*'
```

<i>по умолчанию, параметр закомментирован и настроен на прослушивание запросов только с локального сетевого интерфейса.</i>


В файле конфигурации `pg_hba.conf` добавляем строку:

```editorconfig
host     all     all    <ip_address>/32     password
```