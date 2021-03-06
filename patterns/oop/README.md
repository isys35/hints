<h1>ООП</h1>

<h2>Принципы</h2>

<b>Инкапсуляция </b> - <i>ограничение доступа</i> к составляющим объект компонентам (методам и переменным). 
Инкапсуляция делает некоторые из компонент доступными только внутри класса.
Выражается в методах с нижним подчёркиванием.

```python
class A:
    def _private(self):
        print('Это приватный метод')


class B:
    def __private(self):
        """Даёт  большую защиту: становится недоступным по этому имени"""
        print('Это приватный метод')
```


<b>Наследование </b> - позволяет создавать класс на основе уже существуещего класса, <i>наследуя</i>
методы и атрибуты класса родителя.

```python
class Parent:  # объявляем родительский класс
    parent_attr = 100

    def __init__(self):
        print('Вызов родительского конструктора')

    def parent_method(self):
        print('Вызов родительского метода')

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        print('Атрибут родителя: {}'.format(Parent.parent_attr))


class Child(Parent):  # объявляем класс наследник
    def __init__(self):
        print('Вызов конструктора класса наследника')

    def child_method(self):
        print('Вызов метода класса наследника')


c = Child()  # экземпляр класса Child
c.child_method()  # вызов метода child_method
c.parent_method()  # вызов родительского метода parent_method
c.set_attr(200)  # еще раз вызов родительского метода
c.get_attr()  # снова вызов родительского метода
```


<b>Полиморфизм </b> - <i>разное поведение</i> одного и того же метода в разных классах.

```python
num1 = 1
num2 = 2
print(num1 + num2)
num1 = "1"
num2 = "2"
print(num1 + num2)
```


<hr>
<i>Много полезной информации в книге "Изучаем Python". Том 2. Марк Лутц. Часть VI</i>