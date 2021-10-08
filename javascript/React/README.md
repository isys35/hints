<h1>React</h1>
<hr>
<h3>Hello world:</h3>

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

ReactDOM.render(
  <h1>Привет, мир!</h1>,
  document.getElementById('root')
);
```
<hr>
<h3>Функциональные и классовые компоненты</h3>

Это 
```javascript
function Welcome(props) {
  return <h1>Привет, {props.name}</h1>;
}
```
Тоже самое что и это
```javascript
class Welcome extends React.Component {
  render() {
    return <h1>Привет, {this.props.name}</h1>;
  }
}
```
<b>Компонент с конструктором класса с начальные состоянием</b>
```javascript
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};  }

  render() {
    return (
      <div>
        <h1>Привет, мир!</h1>
        <h2>Сейчас {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```
<hr>


<b>Компоненты жизненного цикла</b>

<img src="lifecicle.png" alt="LifeCicle">


