# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saumariapp', '0003_auto_20150914_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(default=b'none', max_length=200),
            preserve_default=True,
        ),
    ]
