<h1>Выполнение упраженений https://sql-ex.ru/</h1>

<h2>Компьютерная фирма: </h2>
Схема БД состоит из четырех таблиц:

Product(maker, model, type)

PC(code, model, speed, ram, hd, cd, price)

Laptop(code, model, speed, ram, hd, price, screen)

Printer(code, model, color, type, price)

Таблица Product представляет производителя (maker), номер модели (model) и тип ('PC' - ПК, 'Laptop' - ПК-блокнот или 'Printer' - принтер). Предполагается, что номера моделей в таблице Product уникальны для всех производителей и типов продуктов. В таблице PC для каждого ПК, однозначно определяемого уникальным кодом – code, указаны модель – model (внешний ключ к таблице Product), скорость - speed (процессора в мегагерцах), объем памяти - ram (в мегабайтах), размер диска - hd (в гигабайтах), скорость считывающего устройства - cd (например, '4x') и цена - price. Таблица Laptop аналогична таблице РС за исключением того, что вместо скорости CD содержит размер экрана -screen (в дюймах). В таблице Printer для каждой модели принтера указывается, является ли он цветным - color ('y', если цветной), тип принтера - type (лазерный – 'Laser', струйный – 'Jet' или матричный – 'Matrix') и цена - price.

<hr>

<h2>Корабли: </h2>
Рассматривается БД кораблей, участвовавших во второй мировой войне. Имеются следующие отношения:

Classes (class, type, country, numGuns, bore, displacement)

Ships (name, class, launched)

Battles (name, date)

Outcomes (ship, battle, result)


Корабли в «классах» построены по одному и тому же проекту, и классу присваивается либо имя первого корабля, построенного по данному проекту, либо названию класса дается имя проекта, которое не совпадает ни с одним из кораблей в БД. Корабль, давший название классу, называется головным.
Отношение Classes содержит имя класса, тип (bb для боевого (линейного) корабля или bc для боевого крейсера), страну, в которой построен корабль, число главных орудий, калибр орудий (диаметр ствола орудия в дюймах) и водоизмещение ( вес в тоннах). В отношении Ships записаны название корабля, имя его класса и год спуска на воду. В отношение Battles включены название и дата битвы, в которой участвовали корабли, а в отношении Outcomes – результат участия данного корабля в битве (потоплен-sunk, поврежден - damaged или невредим - OK).
Замечания. 1) В отношение Outcomes могут входить корабли, отсутствующие в отношении Ships. 2) Потопленный корабль в последующих битвах участия не принимает.


<h2>Фирма вторсырья: </h2>
Фирма имеет несколько пунктов приема вторсырья. Каждый пункт получает деньги для их выдачи сдатчикам вторсырья. Сведения о получении денег на пунктах приема записываются в таблицу:
Income_o(point, date, inc)
Первичным ключом является (point, date). При этом в столбец date записывается только дата (без времени), т.е. прием денег (inc) на каждом пункте производится не чаще одного раза в день. Сведения о выдаче денег сдатчикам вторсырья записываются в таблицу:
Outcome_o(point, date, out)
В этой таблице также первичный ключ (point, date) гарантирует отчетность каждого пункта о выданных деньгах (out) не чаще одного раза в день.
В случае, когда приход и расход денег может фиксироваться несколько раз в день, используется другая схема с таблицами, имеющими первичный ключ code:
Income(code, point, date, inc)
Outcome(code, point, date, out)
Здесь также значения столбца date не содержат времени.



<hr>

<h3>1</h3> <b>Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол. Вывести: model, speed и hd</b>

```sql
SELECT model, speed, hd FROM PC WHERE price<500;
```

<h3>2</h3> <b>Найдите производителей принтеров. Вывести: maker </b>

```sql
SELECT DISTINCT maker FROM Product WHERE type='Printer';
```

<h3>3</h3> <b>Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 дол. </b>

```sql
SELECT model, ram, screen FROM Laptop WHERE price > 1000;
```

<h3>4</h3> <b>Найдите все записи таблицы Printer для цветных принтеров.  </b>

```sql
SELECT * FROM Printer WHERE color = 'y';
```

<h3>5</h3> <b>Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.  </b>

```sql
SELECT model, speed, hd FROM PC
    WHERE cd IN ('12x', '24x') AND price < '600';
```

<h3>6</h3> <b>Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не менее 10 Гбайт, найти скорости таких ПК-блокнотов. 
Вывод: производитель, скорость. </b>

```sql
SELECT DISTINCT Product.maker, Laptop.speed
    FROM Product JOIN 
     Laptop ON Product.model = Laptop.model 
    WHERE Laptop.hd >= 10;
```


<h3>7</h3> <b>Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).  </b>

```sql
SELECT DISTINCT PC.model, PC.price from PC
 INNER JOIN Product ON PC.model = Product.model
 WHERE Product.maker = 'B'

UNION

SELECT DISTINCT Laptop.model, Laptop.price from Laptop
 INNER JOIN Product ON Laptop.model = Product.model
 WHERE Product.maker = 'B'

UNION

SELECT DISTINCT Printer.model, Printer.price from Printer
 INNER JOIN Product ON Printer.model = Product.model
 WHERE Product.maker = 'B'
```

<h3>8</h3> <b>Найдите производителя, выпускающего ПК, но не ПК-блокноты.   </b>

```sql
SELECT DISTINCT maker FROM Product
    WHERE type = 'PC' 
      AND maker NOT IN 
          (SELECT DISTINCT maker FROM Product WHERE type = 'Laptop');
```

<h3>9</h3> <b>Найдите производителей ПК с процессором не менее 450 Мгц. Вывести: Maker</b>

```sql
SELECT DISTINCT maker
FROM Product INNER JOIN 
 PC ON PC.model = Product.model
WHERE PC.speed >= '450';
```


<h3>10</h3> <b>Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price </b>

```sql
SELECT model, price FROM Printer 
    WHERE price = (SELECT MAX(price) from Printer);
```


<h3>11</h3> <b>Найдите среднюю скорость ПК. </b>

```sql
SELECT AVG(speed) FROM PC;
```

<h3>12</h3> <b>Найдите среднюю скорость ПК-блокнотов, цена которых превышает 1000 дол. </b>

```sql
SELECT AVG(speed) FROM Laptop WHERE price > '1000';
```

<h3>13</h3> <b>Найдите среднюю скорость ПК, выпущенных производителем A.  </b>

```sql
SELECT AVG(PC.speed) 
FROM PC 
INNER JOIN Product ON Product.model = PC.model
WHERE Product.maker = 'A';
```


<h3>14</h3> <b>Найдите класс, имя и страну для кораблей из таблицы Ships, имеющих не менее 10 орудий.  </b>

```sql
SELECT Ships.class, Ships.name, Classes.country 
    FROM Ships 
        INNER JOIN Classes ON Classes.class = Ships.class 
    WHERE Classes.numGuns >= 10;
```

<h3>15</h3> <b>Найдите размеры жестких дисков, совпадающих у двух и более PC. Вывести: HD  </b>

```sql
SELECT hd FROM PC GROUP BY hd HAVING COUNT(hd) >= '2';
```

<h3>16</h3> <b>Найдите пары моделей PC, имеющих одинаковые скорость и RAM. В результате каждая пара указывается только один раз, т.е. (i,j), но не (j,i), Порядок вывода: модель с большим номером, модель с меньшим номером, скорость и RAM.</b>

```sql
SELECT DISTINCT A.model AS model_1, B.model AS model_2, A.speed, A.ram
    FROM PC AS A, PC B
    WHERE A.speed = B.speed AND A.ram = B.ram AND
A.model > B.model;
```

<h3>17</h3> <b>Найдите модели ПК-блокнотов, скорость которых меньше скорости каждого из ПК. Вывести: type, model, speed </b>

```sql
SELECT DISTINCT Product.type, Laptop.model, Laptop.speed 
    FROM Laptop 
        INNER JOIN Product ON Product.model=Laptop.model 
WHERE Laptop.speed < ALL (SELECT speed FROM PC)
```


<h3>18</h3> <b>Найдите производителей самых дешевых цветных принтеров. Вывести: maker, price </b>

```sql
SELECT DISTINCT Product.maker, Printer.price 
    FROM Printer 
        INNER JOIN Product ON Product.model = Printer.model 
                                  AND Printer.color = 'y' 
                                  AND Printer.price = 
                                      (SELECT MIN(price) FROM Printer WHERE color = 'y')
```


<h3>19</h3> <b>Для каждого производителя, имеющего модели в таблице Laptop, найдите средний размер экрана выпускаемых им ПК-блокнотов. Вывести: maker, средний размер экрана.  </b>

```sql
SELECT Product.maker, AVG(Laptop.screen) 
    from Laptop 
        INNER JOIN Product ON Laptop.model = Product.model 
GROUP BY Product.maker
```

<h3>20</h3> <b>Найдите производителей, выпускающих по меньшей мере три различных модели ПК. Вывести: Maker, число моделей ПК.   </b>

```sql
SELECT maker, count(model) 
    FROM Product 
WHERE type='PC' GROUP BY maker HAVING count(model)>2;
```

<h3>21</h3> <b>Найдите максимальную цену ПК, выпускаемых каждым производителем, у которого есть модели в таблице PC. Вывести: maker, максимальная цена.    </b>

```sql
SELECT Product.maker, max(PC.price) 
    FROM PC 
        INNER JOIN Product ON Product.model = PC.model 
GROUP BY Product.maker;
```

<h3>22</h3> <b>Для каждого значения скорости ПК, превышающего 600 МГц, определите среднюю цену ПК с такой же скоростью. Вывести: speed, средняя цена. </b>

```sql
SELECT speed, avg(price) 
    FROM PC WHERE speed > '600' 
GROUP BY speed;
```


<h3>23</h3> <b>Найдите производителей, которые производили бы как ПК
со скоростью не менее 750 МГц, так и ПК-блокноты со скоростью не менее 750 МГц.
Вывести: Maker </b>

```sql
SELECT maker
   FROM PC
   JOIN Product ON PC.model = Product.model
   WHERE speed >= '750'
INTERSECT
SELECT maker 
   FROM Laptop
   JOIN Product ON Laptop.model = Product.model
   WHERE speed >= '750'
```

<h3>24</h3> <b>Перечислите номера моделей любых типов, имеющих самую высокую цену по всей имеющейся в базе данных продукции. </b>

```sql
WITH prices AS (SELECT model, price FROM PC
    UNION
 SELECT model, price FROM Laptop
    UNION 
 SELECT model, price FROM Printer)
SELECT model FROM prices WHERE price= (SELECT MAX(price) FROM prices);
```


<h3>25</h3> <b>Найдите производителей принтеров, которые производят ПК с наименьшим объемом RAM и с самым быстрым процессором 
среди всех ПК, имеющих наименьший объем RAM. Вывести: Maker </b>

```sql
SELECT DISTINCT maker
    FROM Product 
    WHERE type = 'printer' AND 
          maker IN(SELECT maker 
                   FROM Product 
                   WHERE model IN(SELECT model 
                                  FROM PC
                                  WHERE speed = (SELECT MAX(speed)
                                                 FROM (SELECT speed 
                                                       FROM PC 
                                                       WHERE ram=(SELECT MIN(ram)
                                                                  FROM PC
                                                                  )
                                                       ) AS z4
                                                 )
                                  )
                   ) 
                        AND 
          maker IN (SELECT maker 
                    FROM Product 
                    WHERE model  IN(SELECT model
                                    FROM PC 
                                    WHERE ram=(SELECT Min(ram) 
                                               FROM PC)
                        )
                )
```


<h3>26</h3> <b>Найдите среднюю цену ПК и ПК-блокнотов, выпущенных производителем A (латинская буква).
Вывести: одна общая средняя цена. </b>

```sql
select AVG(price) FROM (SELECT price FROM PC WHERE model IN (SELECT model from Product WHERE maker = 'A')
    UNION ALL
SELECT price FROM Laptop WHERE model IN (SELECT model from Product WHERE maker = 'A') ) as prices
```

<h3>27</h3> <b>Найдите средний размер диска ПК каждого из тех производителей, которые выпускают и принтеры. 
Вывести: maker, средний размер HD. </b>

```sql
SELECT maker, AVG(hd)
FROM product t1 JOIN pc t2 ON t1.model=t2.model
WHERE maker IN (
SELECT maker
FROM product
WHERE type='printer'
)
GROUP BY maker
```


<h3>28</h3> <b>Используя таблицу Product, определить количество производителей, выпускающих по одной модели.  </b>

```sql
SELECT count(count_maker)
FROM (
    SELECT count(maker) as count_maker 
    FROM Product 
    GROUP BY maker
    HAVING count(maker)=1
    ) 
    AS x;
```



<h3>29</h3> <b>В предположении, что приход и расход денег на каждом пункте приема фиксируется не чаще одного раза в день [т.е. первичный ключ (пункт, дата)], написать запрос с выходными данными (пункт, дата, приход, расход). Использовать таблицы Income_o и Outcome_o.   </b>


```sql
SELECT
 CASE
  WHEN t1.point IS NULL
  THEN t2.point
  ELSE t1.point
  END point,
 CASE
  WHEN t1.date IS NULL
  THEN t2.date
  ELSE t1.date
  END point,
inc, out
 FROM Income_o as t1 FULL JOIN Outcome_o as t2 ON t1.point = t2.point AND t1.date = t2.date;
```

<h3>30</h3> <b>В предположении, что приход и расход денег на каждом пункте приема фиксируется произвольное число раз 
(первичным ключом в таблицах является столбец code), требуется получить таблицу, в которой каждому пункту за каждую дату 
выполнения операций будет соответствовать одна строка.
Вывод: point, date, суммарный расход пункта за день (out), суммарный приход пункта за день (inc). 
Отсутствующие значения считать неопределенными (NULL).    </b>

```sql
SELECT CASE
  WHEN t1.point IS NULL
  THEN t2.point
  ELSE t1.point
  END point,
 CASE
  WHEN t1.date IS NULL
  THEN t2.date
  ELSE t1.date
  END point, outcome, income FROM
 (SELECT  point, date, SUM(inc) as income FROM Income 
      GROUP BY point, date) t1 
FULL JOIN 
  (SELECT point, date, SUM(out) as outcome FROM Outcome 
       GROUP BY point, date) t2 
ON t1.point = t2.point AND t1.date = t2.date
```

<h3>31</h3> <b>Для классов кораблей, калибр орудий которых не менее 16 дюймов, укажите класс и страну.    </b>


```sql
SELECT class, country FROM Classes WHERE bore >= '16';
```


<h3>32</h3> <b>Одной из характеристик корабля является половина куба калибра его главных орудий (mw). С точностью до 2 десятичных знаков определите среднее значение mw для кораблей каждой страны, у которой есть корабли в базе данных.</b>


```sql
SELECT country, CONVERT(NUMERIC(10,2),AVG(bore*bore*bore/2)) weight
FROM (SELECT country,bore,name
    FROM Classes
    RIGHT JOIN Ships ON Ships.class = Classes.class 
    UNION
    SELECT DISTINCT country, bore, ship
    FROM Classes c 
    LEFT JOIN Outcomes o ON o.ship = c.class
    WHERE  NOT EXISTS(SELECT name
    FROM Ships
    WHERE name = o.ship) AND 
    NOT (ship IS NULL)
 ) as t
GROUP BY country
```


<h3>33</h3> <b>Укажите корабли, потопленные в сражениях в Северной Атлантике (North Atlantic). Вывод: ship.</b>


```sql
SELECT ship FROM Outcomes WHERE result = 'sunk' AND battle='North Atlantic'
```


<h3>34</h3> <b>По Вашингтонскому международному договору от начала 1922 г. запрещалось строить линейные корабли водоизмещением более 35 тыс.тонн. Укажите корабли, нарушившие этот договор (учитывать только корабли c известным годом спуска на воду). Вывести названия кораблей. </b>


```sql
SELECT name
FROM Ships, Classes
WHERE launched >=1922
AND displacement >35000
AND Classes.class = Ships.class
AND type='bb'
```

<h3>35</h3> <b>В таблице Product найти модели, которые состоят только из цифр или только из латинских букв (A-Z, без учета регистра).
Вывод: номер модели, тип модели.  </b>


```sql
SELECT model,type FROM Product
WHERE  model NOT LIKE '%[^0-9]%' OR model NOT LIKE '%[^a-zA-Z]%'
```