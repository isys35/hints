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