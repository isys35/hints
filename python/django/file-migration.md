<h1>Измение данных в сочетании со схемой</h1>

<h3>Создание пустого файла миграции</h3>

```shell
python manage.py makemigrations --empty yourappname
```

<h3>Создание начальный данных</h3>

```python
from django.db import migrations

def combine_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Person = apps.get_model('yourappname', 'Person')
    for person in Person.objects.all():
        person.name = '%s %s' % (person.first_name, person.last_name)
        person.save()

class Migration(migrations.Migration):

    dependencies = [
        ('yourappname', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
```