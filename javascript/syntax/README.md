<h1>Синтаксис JavaScript</h1>

<h3>Стрелочные функции</h3>

<hr>
<b>Однострочные стрелочные функции</b>

Это 
```javascript
let sum = function(a, b) {
  return a + b;
};
```
Тоже самой что и это:
```javascript
let sum = (a, b) => a + b
```

<b>Многострочные стрелочные функции</b>

Это 
```javascript
let sum = function(a, b) {
    let result = a + b;
  return result;
};
```
Тоже самой что и это:
```javascript
let sum = (a, b) => {  
  let result = a + b;
  return result; 
};
```
<hr>

<h3>Работа с массивами</h3>

<b>map</b> -  вызывает функцию для каждого элемента массива и возвращает массив результатов выполнения этой функции.

```javascript
let lengths = ["Bilbo", "Gandalf", "Nazgul"].map(item => item.length);
// length = [5,7,6]
```
<hr>
<h3>Условные и логические операторы</h3>

<b>if c одной ветвью</b>

Синтаксис:

```javascript
if (условие)
  инструкция
```

Пример:

```javascript
if (true)
  count = 4;
```

Если необходимо выполнить несколько инструкций

```javascript
if (typeof votes === 'number') {
  votes++;
  console.log('Число голосов: ' + votes);
}
```

<b>if..else c двумя ветвями</b>

Синтаксис:

```javascript
if (условие) {
  одно или несколько инструкций (будут выполняться, когда условие равно true или приведено к true)
} else {
  одно или несколько инструкций (будут выполняться, когда условие равно false или приведено к false)
}
```

Пример

```javascript
if (number % 2) {
  console.log('Число нечётное!');
} else {
  console.log('Число чётное!');
}
```

<b>Тернарный оператор</b>

Синтаксис
```javascript
условие ? выражение1 : выражение2
```

Пример
```javascript
(number % 2) ? console.log('Число нечётное!') : console.log('Число чётное!');
```

<b>if..else множество условий</b>

Синтаксис:

```javascript
if (условие1) {
  инструкции 1
} else if (условие2) {
  инструкции 2
} else if (условие3) {
  инструкции 3
//...
} else if (условиеN) {
  инструкции N
} else {
  инструкции, которые будут выполнены, если ни одно из условий не равно true или не приведёно к этом значению 
}
```

В JavaScript допустимы множественные тернарные операторы (?:):


```javascript
var dayNumber = new Date().getDay();

day =
  (dayNumber === 0) ? 'Воскресенье' :
    (dayNumber === 1) ? 'Понедельник' :
      (dayNumber === 2) ? 'Вторник' :
        (dayNumber === 3) ? 'Среда' :
          (dayNumber === 4) ? 'Четверг' :
            (dayNumber === 5) ? 'Пятница' :
              (dayNumber === 6) ? 'Суббота' : 'Неизвестный день недели';

console.log('Сегодня ' + day.toLowerCase() + '.');
```