<h1>S.O.L.I.D.</h1>
<details><summary>Что это?</summary>Аббревиатура для набора принципов проектирования</details>
<hr>
<h3>Single Responsibility Principle (Принцип единственной ответственности)</h3>
Один класс отвечает только за что-то одно (Выполняет только одну работу)

**НЕПРАВИЛЬНО**
```python
# Below is Given a class which has two responsibilities 
class  User:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, user: User):
        pass
```
**ПРАВИЛЬНО**
```python
class User:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class UserDB:
    def get_user(self, id) -> User:
        pass

    def save(self, user: User):
        pass
```
<hr>
<h3>Open-Closed Principle (Принцип открытости/закрытости)</h3>
Программные сущности (классы, модули, функции) должно быть открыты для расширения, но закрыты для модификации.

**НЕПРАВИЛЬНО**

```python
class Discount:
  def __init__(self, customer, price):
      self.customer = customer
      self.price = price
      
  def give_discount(self):
      if self.customer == 'fav':
          return self.price * 0.2
      if self.customer == 'vip':
          return self.price * 0.4
```

**ПРАВИЛЬНО**
```python
class Discount:
    def __init__(self, customer, price):
      self.customer = customer
      self.price = price
    def get_discount(self):
      return self.price * 0.2

class VIPDiscount(Discount):
    def get_discount(self):
      return super().get_discount() * 2

```

Расширять, но не модифицировать!
<hr>
<h3>Liskov Substitution Principle (Принцип подстановки Лисков)</h3>
Для любого класса клиент должен иметь возможность использовать любой подкласс базового класса, 
не замечая разницы между ними.

Формально: Пусть q(x) является свойством, верным относительно объектов x некоторого типа T. Тогда q(y) также должно
быть верным для объектов y типа S, где S является подтипом типа T.

Просто: подкласс, дочерний класс должны соответствовать их родительскому классу или супер классу.

```python
class Rectangle:
    
    def __init__(self, height, width):
        self._height = height
        self._width = width    @property
        
    def width(self):
        return self._width    @width.setter
    
    def width(self, value):
        self._width = value    @property
        
    def height(self):
        return self._height    @height.setter
    
    def height(self, value):
        self._height = value
        
    def get_area(self):
        return self._width * self._height
    
    
class Square(Rectangle):
    
    def __init__(self, size):
        Rectangle.__init__(self, size, size)    
        
    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value   
    
    @Rectangle.height.setter
    def height(self, value):
        self._width = value
        self._height = value
        
        
def get_squashed_height_area(Rectangle):
    Rectangle.height = 1
    area = Rectangle.get_area()
    return area


rectangle = Rectangle(5, 5)
square = Square(5)

assert get_squashed_height_area(rectangle) == 5  # expected 5
assert get_squashed_height_area(square) == 1  # expected 5
```
<hr>
<h3>Interface Segregation Principle (Принцип разделения интерфейсов)</h3>
Создавайте узкоспециализированные интерфейсы, предназначенные для конкретного клиента. 
Клиенты не должны зависеть от интерфейсов, которые они не используют.

```python
class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass
```
<hr>
<h3>Dependecy Inversion Principle (Принцип инверсии зависимостей)</h3>
Зависимость должна быть от абстракций,  а не от конкретики.

```python
# define a common interface any food should have and implement
class IFood:
    
    def bake(self): pass
    
    def eat(self): pass

class Bread(IFood):
    
    def bake(self):
        print("Bread was baked")
        
    def eat(self):
        print("Bread was eaten")

class Pastry(IFood):
    
    def bake(self):
        print("Pastry was baked")
        
    def eat(self):
        print("Pastry was eaten")

class Production:
    
    def __init__(self, food): # food now is any concrete implementation of IFood
        self.food = food # this is also dependnecy injection, as it is a parameter not hardcoded

    def produce(self):
        self.food.bake()  # uses only the common interface

    def consume(self):
        self.food.eat()  # uses only the common interface

```
