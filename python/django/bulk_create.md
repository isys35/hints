<h1>bulk_create()</h1>

```python
objs = Entry.objects.bulk_create([
            Entry(headline='This is a test'),
            Entry(headline='This is only a test')])
```