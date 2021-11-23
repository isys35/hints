<h2>Фабричный метод</h2> - решает проблему создания различных продуктов, 
без указания конкретных классов продуктов.

Фабричный метод задаёт метод, который следует использовать для создания объектов-продуктов.

**Применимость:** там где требуется гибкость для создания продуктов.

<a href='https://github.com/isys35/hints/blob/master/patterns/codes/factory_method.py'>Пример</a>



<h2>Абстрактная фабрика</h2> - это порождающий паттерн проектирования, который позволяет создавать семейства связанных 
объектов, не привязываясь к конкретным классам создаваемых объектов.

**Применимость:** Когда бизнес-логика программы должна работать с разными видами связанных друг с другом продуктов, не завися от конкретных классов продуктов.
Когда в программе уже используется Фабричный метод, но очередные изменения предполагают введение новых типов продуктов.

<a href='https://github.com/isys35/hints/blob/master/patterns/codes/abstract_factory.py'>Пример</a>



<h2>Строитель</h2> - это порождающий паттерн проектирования, который позволяет создавать объекты пошагово

**Применимость:** там, где требуется пошаговое создание продуктов или конфигурация сложных объектов.

<a href='https://github.com/isys35/hints/blob/master/patterns/codes/builder.py'>Пример</a>