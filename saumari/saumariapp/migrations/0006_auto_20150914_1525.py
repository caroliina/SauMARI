# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saumariapp', '0005_auto_20150914_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='listing',
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.ForeignKey(default=1, to='saumariapp.Type'),
            preserve_default=True,
        ),
    ]
