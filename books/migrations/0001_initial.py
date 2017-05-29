# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateField(null=True, verbose_name=b'date published', blank=True)),
                ('text', models.TextField(blank=True)),
                ('isbn', models.CharField(max_length=200, blank=True)),
                ('genre', models.CharField(max_length=50, choices=[(b'ROMANCE', b'Romance'), (b'EROTICA', b'Erotica')])),
                ('cover_image', models.CharField(max_length=200)),
                ('publisher_link', models.URLField()),
                ('excerpt', models.URLField(null=True, blank=True)),
                ('author', models.CharField(max_length=50, choices=[(b'MEG', b'Meg Maguire'), (b'CARA', b'Cara McKenna')])),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('url', models.URLField()),
                ('source', models.CharField(max_length=255, blank=True)),
                ('book', models.ForeignKey(to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VendorLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('format', models.CharField(max_length=50, choices=[(b'EBOOK', b'e-book'), (b'PAPERBACK', b'paperback'), (b'AUDIO', b'audio')])),
                ('book', models.ForeignKey(to='books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, to='books.Publisher', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='theme',
            field=models.ManyToManyField(to='books.Theme', blank=True),
        ),
    ]
