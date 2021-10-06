<h1>SQL</h1>

<h2>SELECT</h2>


Оператор SELECT осуществляет выборку из базы данных


Пример выборки всех данных:

```sql
    SELECT * FROM PC;
```

Пример выборки определённых полей в определённом порядке данных:

```sql
    SELECT price, speed, hd
    FROM PC;
```


<h2>DISTINCT</h2>

Выводит уникальные строки

```sql
    SELECT DISTINCT speed, ram 
    FROM PC;
```

