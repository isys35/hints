<h1>FastAPI</h1>

**Установка**

```shell
pip install fastapi
```

```shell
pip install uvicorn
```


**Привет мир**

<a href="/main.py">main.py</a>

```shell
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

Запуск:

```shell
uvicorn main:app --reload
```