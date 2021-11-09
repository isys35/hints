<h1>Рефы</h1>

Рефы дают возможность получить доступ к DOM-узлам или React-элементам, 
созданным в рендер-методе.

<h3>Когда использовать рефы</h3>

<ul>
    <li>Управление фокусом, выделение текста или воспроизведение медиа.</li>
    <li>Императивный вызов анимаций</li>
    <li>Интеграция со сторонними DOM-библиотеками.</li>
</ul>

Пример

```javascript
class CustomTextInput extends React.Component {
  constructor(props) {
    super(props);
    // создадим реф в поле `textInput` для хранения DOM-элемента
    this.textInput = React.createRef();  
    this.focusTextInput = this.focusTextInput.bind(this);
  }

  focusTextInput() {
    // Установим фокус на текстовое поле с помощью чистого DOM API
    // Примечание: обращаемся к "current", чтобы получить DOM-узел
    this.textInput.current.focus();  }

  render() {
    // описываем, что мы хотим связать реф <input>
    // с `textInput` созданным в конструкторе
    return (
      <div>
        <input
          type="text"
          ref={this.textInput} />
        <input
          type="button"
          value="Фокус на текстовом поле"
          onClick={this.focusTextInput}
        />
      </div>
    );
  }
}
```