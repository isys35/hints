<h1>Docker</h1>

Список образов:

```shell
docker images
```

Запуск образа:

```shell
docker run <image_name>
```

Запуск образа в интерактивном режиме.

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

Запуск образа в интерактивнои режиме 
с открытым портом и с конфигурацией с переменными окружения
```shell
docker run --name <name container> --env-file <env filename> -p <inner port>:<outer port> -it <image_name> bash
```

Создание и запуск контейнера:
```shell
docker-compose up -d
```

Остановка и удаление контейнеров:
```shell
docker-compose down
```

Подключится к работающему контейнеру
```shell
docker exec -it <container id> bash 
```

Делает build для всех образов указанных в docker-compose.yml
```shell
docker-compose build
```

