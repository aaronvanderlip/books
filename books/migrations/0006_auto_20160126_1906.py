# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_series_seriesentry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.AlterModelOptions(
            name='seriesentry',
            options={'verbose_name_plural': 'Series Entries'},
        ),
        migrations.RenameField(
            model_name='seriesentry',
            old_name='sequene',
            new_name='number',
        ),
    ]
