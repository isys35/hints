<h1>SQLAlchemy</h1>

**Соединение с базой данных**

```python
from sqlalchemy import create_engine
engine = create_engine('postgresql://usr:pwd@localhost:5432/db', echo=True)
```

Создание декларативного расширения.(Лаконичное отображение стиля работы ORM)

```python
from sqlalchemy.orm import declarative_base
Base = declarative_base()
```

#TODO доделать