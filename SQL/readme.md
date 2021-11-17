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



<h2>Предикаты</h2>

Предикаты представляют собой выражения, 
принимающие истинностное значение. 
Они могут представлять собой как одно выражение,
так и любую комбинацию из неограниченного количества выражений, 
построенную с помощью булевых операторов AND, OR или NOT. 
Кроме того, в этих комбинациях может использоваться SQL-оператор 
IS, а также круглые скобки для конкретизации.


<h2>JOIN</h2>

Объединяет таблицы.

Как оформляется:

```sql
    FROM <таблица 1>
     [INNER]
     {{LEFT | RIGHT | FULL } [OUTER]} JOIN <таблица 2>
    [ON <предикат>]
```



<h2>UNION</h2>

Объединяет запросы.


```sql
    <запрос 1>
    UNION [ALL]
    <запрос 2>
```


<h2>INTERSECT и EXCEPT</h2>

Пересечение и разность

Пример: Найти корабли, которые присутствуют как в таблице Ships,
так и в таблице Outcomes. 

```sql
    SELECT name FROM Ships
    INTERSECT
    SELECT ship FROM Outcomes;
```

Пример: Найти корабли из таблицы Outcomes,
которые отсутствуют в таблице Ships. 

```sql
    SELECT ship FROM Outcomes
    EXCEPT
    SELECT name FROM Ships;
```


<h2>IN</h2>

Предикат IN определяет, будет ли значение проверяемого выражения обнаружено в наборе значений, который либо явно 
либо получен с помощью табличного подзапроса.


```sql
    IN::=
     <Проверяемое выражение> [NOT] IN (<подзапрос>)
     | (<выражение для вычисления значения>,...)
```

Пример: Найти модель, частоту процессора и объем жесткого диска компьютеров, которые комплектуются накопителями 10 Гбайт
или 20 Гбайт и выпускаются производителем А:

```sql
    SELECT model, speed, hd
    FROM PC 
    WHERE hd IN (10, 20) AND 
     model IN (SELECT model 
     FROM product 
     WHERE maker = 'A'
     );
```


<h2>Подзапросы</h2>

Пример: Найти модели и цены ПК, стоимость которых превышает минимальную стоимость портативных компьютеров:


```sql
    SELECT DISTINCT model, price
    FROM PC
    WHERE price > (SELECT MIN(price) 
     FROM Laptop
     );
```


<h2>Агрегатные функции</h2>


Агрегатные функции:
    <ul>
        <li>`COUNT(*)` - Возвращает количество строк источника записей</li>
        <li>`COUNT` - Возвращает количество значений в указанном столбце</li>
        <li>`SUM` -  Возвращает сумму значений в указанном столбце</li>
        <li>`AVG` -  Возвращает среднее значение в указанном столбце</li>
        <li>`MIN` -  Возвращает минимальное значение в указанном столбце</li>
        <li>`MAX` -  Возвращает максимальное значение в указанном столбце</li>
    </ul>


Пример: Найти минимальную и максимальную цену на персональные компьютеры:

```sql
    SELECT MIN(price) AS Min_price, 
        MAX(price) AS Max_price
    FROM PC;
```


<h2>GROUP BY</h2>
Предложение GROUP BY используется для определения групп выходных строк, к которым могут применяться агрегатные функции (COUNT, MIN, MAX, AVG и SUM).



<h2>HAVING</h2>
<b>HAVING</b> - применяется после группировки для определения аналогичного предиката, фильтрующего группы по значениям агрегатных функций

Пример: Получить количество ПК и среднюю цену для каждой модели, средняя цена которой менее $800 


```sql
    SELECT model, COUNT(model) AS Qty_model, 
       AVG(price) AS Avg_price
    FROM PC
    GROUP BY model
    HAVING AVG(price) < 800;
```


<h2>Использование в запросе нескольких источников записей</h2>

Пример: Вывести пары моделей, имеющих одинаковые цены:

```sql
    SELECT DISTINCT A.model AS model_1, B.model AS model_2
    FROM PC AS A, PC AS B
    WHERE A.price = B.price AND 
     A.model < B.model;
```


<h2>SOME(ANY) ALL</h2>

`<выражение> <оператор сравнения> SOME | ANY (<подзапрос>)`

`<выражение> <оператор сравнения> ALL (<подзапрос>)`


Пример: Найти модели и цены портативных компьютеров, стоимость которых превышает стоимость любого ПК 

```sql
    SELECT DISTINCT model, price
    FROM Laptop
    WHERE price > ALL (SELECT price 
     FROM PC
     );
```

<h2>INTERSECT, EXCEPT</h2>

В результирующий набор попадают только те строки, которые присутствуют в обоих запросах (`INTERSECT`) или только те строки первого запроса, которые отсутствуют во втором (`EXCEPT`).

Пример: Найти производителей, которые выпускают не менее двух моделей ПК и не менее двух моделей принтеров.


```sql
    SELECT maker FROM (
    SELECT maker FROM Product WHERE type='PC'
    INTERSECT ALL
    SELECT maker FROM Product WHERE type ='Printer'
    ) X GROUP BY maker HAVING COUNT(*)>1;
```


<h2>CTE</h2>
Общие табличные выражения

Задача:

Найти максимальную сумму прихода/расхода среди всех 4-х таблиц базы данных "Вторсырье", а также тип операции, дату и пункт приема, когда и где она была зафиксирована.

Пример без CTE:

```sql
    SELECT inc AS max_sum, type, date, point 
    FROM ( SELECT inc, 'inc' type, date, point 
    FROM Income UNION ALL SELECT inc, 'inc' type, date, point 
    FROM Income_o 
    UNION ALL 
    SELECT out, 'out' type, date, point 
    FROM Outcome_o 
    UNION ALL 
    SELECT out, 'out' type, date, point FROM Outcome ) X 
    WHERE inc >= ALL( SELECT inc FROM Income 
           UNION ALL 
           SELECT inc FROM Income_o 
           UNION ALL SELECT out FROM Outcome_o 
           UNION ALL SELECT out FROM Outcome );
```


Пример с CTE:
```sql
    WITH Inc_Out AS (  
      SELECT inc, 'inc' type, date, point 
      FROM Income 
      UNION ALL 
      SELECT inc, 'inc' type, date, point 
      FROM Income_o 
      UNION ALL 
      SELECT out, 'out' type, date, point 
      FROM Outcome_o 
      UNION ALL 
      SELECT out, 'out' type,date, point FROM Outcome ) 
    SELECT inc AS max_sum, type, date, point 
    FROM Inc_Out WHERE inc >= ALL ( SELECT inc FROM Inc_Out);
```


<h2>CASE</h2>

Оператор CASE в зависимости от указанных условий возвращает одно из множества возможных значений.


Задача:

Пусть требуется вывести список всех моделей ПК с указанием их цены. При этом если модель отсутствует в продаже (ее нет в таблице РС), 
то вместо цены вывести текст «Нет в наличии».


```sql
    SELECT DISTINCT product.model, 
     CASE 
     WHEN price IS NULL 
     THEN 'Нет в наличии' 
     ELSE CAST(price AS CHAR(20)) 
     END price 
    FROM Product LEFT JOIN 
     PC ON Product.model = PC.model
    WHERE product.type = 'pc';
```


<h2>CAST</h2>

Преобразование типов

```sql
CAST(<выражение> AS <тип данных>)
```

```sql
    SELECT Classes.country, CAST(AVG(POWER(bore, 3)/2) AS DEC(12,2)) as weight FROM Ships RIGHT JOIN Classes ON Ships.class = Classes.class GROUP BY Classes.country
    
```
