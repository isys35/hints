<h3>Запросы</h3>


<h4>Создание объектов</h4>

```python
from blog.models import Blog
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()
```

<h4>Сохранение изменений в объектах</h4>

```python
b5.name = 'New name'
b5.save()
```

<h4>Сохранение полей ForeignKey и ManyToManyField</h4>

```python
from blog.models import Blog, Entry
entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Cheddar Talk")
entry.blog = cheese_blog
entry.save()
```

```python
from blog.models import Author
joe = Author.objects.create(name="Joe")
entry.authors.add(joe)
```

<h4>Получение всех объектов</h4>

```python
all_entries = Entry.objects.all()
```

<h4>Получение определенных объектов с помощью фильтров</h4>

`filter(**kwargs)` - Возвращает новый `QuerySet`, содержащий объекты, которые соответствуют заданным параметрам поиска.

`exclude(**kwargs)` - Возвращает новый `QuerySet`, содержащий объекты, которые <b>не</b> соответствуют указанным параметрам поиска.

```python
Entry.objects.filter(pub_date__year=2006)


Entry.objects.filter(headline__startswith='What').exclude(pub_date__gte=datetime.date.today()).filter(pub_date__gte=datetime.date(2005, 1, 30))
```

<h4>Получение одного объекта</h4>

```python
one_entry = Entry.objects.get(pk=1)
```


<h4>Поиск по полям</h4>

```python
one_entry = Entry.objects.get(pk=1)
```
Справочник по полям: <a href="https://django.fun/docs/django/ru/3.2/ref/models/querysets/#field-lookups">https://django.fun/docs/django/ru/3.2/ref/models/querysets/#field-lookups </a>

Базовые аргументы поиска по ключевым словам имеют вид `field__lookuptype=value`. (Это двойное подчеркивание). Например:

```python
Entry.objects.filter(pub_date__lte='2006-01-01')
```



<h4>Поиск, который использует отношения</h4>

```python
Blog.objects.filter(entry__authors__name='Lennon')
```

<h4>Фильтры c ссылкой на поля модели</h4>

```python
from django.db.models import F
Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))
```

<h4>Кэширование и QuerySet</h4>

Во вновь созданном QuerySet кеш пуст.
 Первый раз QuerySet оценивается и, следовательно, происходит запрос к базе данных -
  Django сохраняет результаты запроса QuerySet в кэш и возвращает результаты, 
  которые были явно запрошены (например, следующий элемент, если итерация происходит через QuerySet). 
  Последующие оценки QuerySet повторно используют кэшированные результаты.
  

<b>Запрос к базе будет выполнен дважды. Неправильно: </b>
```python
print([e.headline for e in Entry.objects.all()])
print([e.pub_date for e in Entry.objects.all()])
```

<b>Правильно: </b>
```python
queryset = Entry.objects.all()
print([p.headline for p in queryset]) # Evaluate the query set.
print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation.
```


<b>Неправильно: </b>

```python
queryset = Entry.objects.all()
print(queryset[5]) # Queries the database
print(queryset[5]) # Queries the database again
```

<b>Правильно: </b>

```python
queryset = Entry.objects.all()
[entry for entry in queryset] # Queries the database
print(queryset[5]) # Uses cache
print(queryset[5]) # Uses cache
```