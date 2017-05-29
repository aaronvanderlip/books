# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20160205_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='related',
            field=models.ManyToManyField(related_name='_book_related_+', to='books.Book'),
        ),
    ]
