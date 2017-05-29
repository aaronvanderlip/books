# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160110_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='thumbnail_image',
            field=models.FileField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(related_name='reviews', to='books.Book'),
        ),
    ]
