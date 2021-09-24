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