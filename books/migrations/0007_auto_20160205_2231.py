# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20160126_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='related',
            field=models.ManyToManyField(to='books.Book'),
        ),
        migrations.AlterField(
            model_name='seriesentry',
            name='book',
            field=models.ForeignKey(related_name='series', to='books.Book'),
        ),
    ]
