# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def set_slug(apps, schema_editor):
     Book = apps.get_model("books", "Book")
     for book in Book.objects.all():
         book.slug = book.title
         book.save()


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20160210_1805'),
    ]

    operations = [
        migrations.RunPython (set_slug),
    ]
