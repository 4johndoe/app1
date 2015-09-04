# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='square',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filiya',
            name='kod',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photo',
            name='file',
            field=models.FilePathField(default=0),
        ),
    ]
