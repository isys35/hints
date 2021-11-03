<h1>БЭМ</h1>

БЭМ (Блок, Элемент, Модификатор) — компонентный подход к веб-разработке. В его основе лежит принцип разделения интерфейса на независимые блок

Блок - Функционально независимый компонент страницы, который может быть повторно использован.
```html
<!-- Блок `header` -->
<header class="header">
    <!-- Вложенный блок `logo` -->
    <div class="logo"></div>

    <!-- Вложенный блок `search-form` -->
    <form class="search-form"></form>
</header>
```

Элемент - Составная часть блока, которая не может использоваться в отрыве от него.

```html
<!-- Блок `search-form` -->
<form class="search-form">
    <!-- Элемент `input` блока `search-form` -->
    <input class="search-form__input">

    <!-- Элемент `button` блока `search-form` -->
    <button class="search-form__button">Найти</button>
</form>
```
<b>Элемент — всегда часть блока, а не другого элемента.</b>


Модификатор - Cущность, определяющая внешний вид, состояние или поведение блока либо элемента.

```html
<!-- Блок `search-form` имеет булевый модификатор `focused` -->
<form class="search-form search-form_focused">
    <input class="search-form__input">

    <!-- Элемент `button` имеет булевый модификатор `disabled` -->
    <button class="search-form__button search-form__button_disabled">Найти</button>
</form>
```

