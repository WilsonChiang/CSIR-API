"""
ISSUE-2: Change maps to map
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('map_url', models.CharField(max_length=255)),
                ('report', models.ForeignKey(to='reports.CountryReport')),
            ],
        ),
        migrations.RemoveField(
            model_name='maps',
            name='report',
        ),
        migrations.DeleteModel(
            name='Maps',
        ),
    ]
