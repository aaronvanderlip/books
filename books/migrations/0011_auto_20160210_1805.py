# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_siteimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, unique=True, null=True, populate_from=b'title'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=50, choices=[(b'ROMANCE', b'Romance'), (b'EROTICA', b'Erotic Romance'), (b'LITERARY', b'Literary Fiction')]),
        ),
    ]
