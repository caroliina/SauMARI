# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('saumariapp', '0002_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='type',
        ),
        migrations.AddField(
            model_name='type',
            name='listing',
            field=models.ForeignKey(default=0, to='saumariapp.Listing'),
            preserve_default=False,
        ),
    ]
