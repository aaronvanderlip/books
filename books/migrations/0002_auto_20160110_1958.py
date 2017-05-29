# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumbnail_image',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
