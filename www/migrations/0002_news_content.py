# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
