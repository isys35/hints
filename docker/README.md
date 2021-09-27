<h1>Docker</h1>

Список образов:

```shell
docker images
```

Запуск образа:

```shell
docker run <image_name>
```

Запуск контейнера в интерактивном режиме.

```shell
docker run --name <name container> -it <image_name> bash
```

Остановка контейнера:
```shell
docker stop <name container>
```

Запуск остановленного контейнера:
```shell
docker start <name container>
```

Удаление контейнера:
```shell
docker rm <name container>
```

Список работающих контейнеров:
```shell
docker ps
```

Подключится к работающему контейнеру
```shell
docker exec -it <container id> bash 
```

Запуск контейнера в интерактивнои режиме 
с открытым портом и с конфигурацией с переменными окружения
```shell
docker run --name <name container> --env-file <env filename> -p <inner port>:<outer port> -it <image_name> bash
```
